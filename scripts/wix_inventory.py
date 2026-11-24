#!/usr/bin/env python3
"""Inventaire complet (lecture seule) d'un blog Wix public.

Usage : python3 scripts/wix_inventory.py <site_wordpress> <url_wix>
  ex. : python3 scripts/wix_inventory.py sabinekouli.com https://matomswe7.wixsite.com/iletaitunevoix

Sources : sitemaps Wix (blog-posts, blog-categories) + liens de navigation de l'accueil.
Sorties dans sites/<site>/wix/ :
  inventory.json, inventory.csv   une ligne par article/page
  content/<slug>.md               texte complet de chaque article (patrimoine, non publié)
Ne modifie rien sur Wix.
"""
import csv, json, re, sys, time, unicodedata
from pathlib import Path
from urllib.parse import unquote, urlparse

import requests
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (compatible; Content-Inventory/1.0; read-only)"


def slugify(s):
    s = unicodedata.normalize("NFKD", unquote(s)).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def locs(sess, url):
    x = sess.get(url, timeout=30).text
    return re.findall(r"<loc>([^<]+)</loc>", x)


def to_markdown(node):
    out = []
    for el in node.find_all(["h1", "h2", "h3", "h4", "p", "li", "blockquote", "img"]):
        if el.find_parent(["li", "blockquote"]) and el.name == "p":
            continue
        if el.name == "img":
            src = el.get("src") or ""
            if "static.wixstatic.com/media" in src:
                out.append(f"![{el.get('alt') or ''}]({src.split('/v1/')[0]})")
            continue
        t = el.get_text(" ", strip=True)
        if not t:
            continue
        pre = {"h1": "# ", "h2": "## ", "h3": "### ", "h4": "#### ", "li": "- ", "blockquote": "> "}.get(el.name, "")
        out.append(pre + t)
    return "\n\n".join(out)


def parse(url, html, kind, base_host):
    s = BeautifulSoup(html, "lxml")
    meta = lambda **kw: (s.find("meta", attrs=kw) or {}).get("content") if s.find("meta", attrs=kw) else None
    art = s.find("article") if kind == "post" else (s.find("main") or s.body)
    ld = []
    for sc in s.find_all("script", type="application/ld+json"):
        try:
            ld.append(json.loads(sc.string or ""))
        except Exception:
            pass
    bp = next((d for d in ld if isinstance(d, dict) and d.get("@type") == "BlogPosting"), {})
    imgs, links_int, links_ext, cats = [], set(), set(), []
    if art:
        for im in art.find_all("img"):
            src = (im.get("src") or "").split("/v1/")[0]
            if "static.wixstatic.com/media" in src:
                imgs.append({"src": src, "alt": im.get("alt") or ""})
        for a in art.find_all("a", href=True):
            h = a["href"]
            if "/blog/categories/" in h:
                cats.append(a.get_text(strip=True))
            elif h.startswith("http"):
                (links_int if urlparse(h).netloc == base_host else links_ext).add(h)
    heads = [(h.name, h.get_text(" ", strip=True)) for h in (art.find_all(["h1", "h2", "h3"]) if art else [])]
    md = to_markdown(art) if art else ""
    words = len(re.findall(r"\w+", art.get_text(" ", strip=True))) if art else 0
    return {
        "kind": kind, "url": url, "slug": slugify(urlparse(url).path.rsplit("/", 1)[-1]) or "accueil",
        "title": s.title.get_text(strip=True) if s.title else None,
        "h1": [t for n, t in heads if n == "h1"],
        "headings": [f"{n}: {t}" for n, t in heads if n != "h1"],
        "meta_description": meta(name="description"),
        "og_description": meta(property="og:description"),
        "robots": meta(name="robots"),
        "canonical": (s.find("link", rel="canonical") or {}).get("href") if s.find("link", rel="canonical") else None,
        "published": meta(property="article:published_time") or bp.get("datePublished"),
        "modified": meta(property="article:modified_time") or bp.get("dateModified"),
        "author": meta(property="article:author"),
        "categories": sorted(set(cats)),
        "words": words, "images": imgs,
        "images_no_alt": sum(1 for i in imgs if not i["alt"].strip()),
        "links_internal": sorted(links_int), "links_external": sorted(links_ext),
        "comments_hint": bool(re.search(r'data-hook="comment', html)),
        "markdown": md,
    }


def main(site, wix):
    wix = wix.rstrip("/")
    host = urlparse(wix).netloc
    out = ROOT / "sites" / site / "wix"
    (out / "content").mkdir(parents=True, exist_ok=True)
    sess = requests.Session(); sess.headers["User-Agent"] = UA
    posts = locs(sess, f"{wix}/blog-posts-sitemap.xml")
    cats = locs(sess, f"{wix}/blog-categories-sitemap.xml")
    home = sess.get(wix, timeout=30).text
    pages = {wix}
    for a in BeautifulSoup(home, "lxml").find_all("a", href=True):
        h = a["href"].split("?")[0].rstrip("/")
        if h.startswith(wix) and "/post/" not in h and "/blog/categories" not in h and "/profile/" not in h:
            pages.add(h)
    items = []
    for kind, urls in (("post", posts), ("category", cats), ("page", sorted(pages))):
        for u in urls:
            r = sess.get(u, timeout=40)
            it = parse(r.url, r.text, kind, host) if r.ok else {"kind": kind, "url": u, "error": r.status_code}
            it["status"] = r.status_code
            items.append(it)
            if kind == "post" and it.get("markdown"):
                hdr = f"---\nsource: {u}\npublished: {it['published']}\nmodified: {it['modified']}\n" \
                      f"categories: {', '.join(it['categories'])}\nwords: {it['words']}\n---\n\n"
                (out / "content" / f"{it['slug']}.md").write_text(hdr + it["markdown"] + "\n")
            time.sleep(0.5)
    (out / "inventory.json").write_text(json.dumps(items, ensure_ascii=False, indent=1))
    with open(out / "inventory.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["kind", "url", "slug", "title", "categories", "published", "words", "meta_description",
                    "h2_h3", "images", "images_no_alt", "links_internal", "links_external", "status"])
        for it in items:
            w.writerow([it["kind"], it["url"], it.get("slug"), it.get("title"), "; ".join(it.get("categories", [])),
                        (it.get("published") or "")[:10], it.get("words"), it.get("meta_description"),
                        " | ".join(it.get("headings", [])), len(it.get("images", [])), it.get("images_no_alt"),
                        len(it.get("links_internal", [])), len(it.get("links_external", [])), it["status"]])
    print(f"{sum(i['kind']=='post' for i in items)} articles, {len(cats)} catégories, {len(pages)} pages -> {out}")


if __name__ == "__main__":
    main(*sys.argv[1:3])
