#!/usr/bin/env python3
"""Audit SEO en LECTURE SEULE d'un site WordPress (niveau 1).

Usage : python3 scripts/audit.py sabinekouli.com

- Inventaire via l'API REST publique (pages, articles, catégories, étiquettes, médias)
- Récupération de l'URL publiée (HTML rendu, après cache LiteSpeed)
- Extraction : statut HTTP, redirections, <title>, meta description, robots,
  canonical, H1/H2/H3, images (alt, dimensions), liens internes/externes,
  JSON-LD, poids HTML, nombre de mots.
- Sorties dans sites/<domaine>/audit/<date>/ : urls.json, urls.csv, summary.md

Aucune requête d'écriture n'est faite. Si un fichier .env.local existe pour le
site, les identifiants sont utilisés UNIQUEMENT pour des lectures (context=edit)
et ne sont jamais écrits dans les sorties.
"""
import csv, datetime as dt, json, re, sys, collections
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).parent))
from wp_client import WPClient  # noqa: E402

UA = "Mozilla/5.0 (compatible; SEO-Audit/1.0; read-only)"


def fetch(session, url):
    r = session.get(url, timeout=30, allow_redirects=True, headers={"User-Agent": UA})
    chain = [f"{h.status_code} {h.url}" for h in r.history]
    return r, chain


def parse_page(url, html, host):
    soup = BeautifulSoup(html, "lxml")
    g = lambda sel, attr="content": (soup.select_one(sel) or {}).get(attr) if soup.select_one(sel) else None
    title = soup.title.get_text(strip=True) if soup.title else None
    hs = {f"h{i}": [h.get_text(" ", strip=True) for h in soup.find_all(f"h{i}")] for i in (1, 2, 3)}
    imgs = []
    for im in soup.find_all("img"):
        src = im.get("data-src") or im.get("src") or ""
        if src.startswith("data:"):
            src = im.get("data-lazyload") or src
        imgs.append({"src": urljoin(url, src)[:300], "alt": im.get("alt"),
                     "w": im.get("width"), "h": im.get("height")})
    internal, external = set(), set()
    for a in soup.find_all("a", href=True):
        href = a["href"].strip()
        if href.startswith(("mailto:", "tel:", "#", "javascript:")):
            continue
        u = urljoin(url, href).split("#")[0]
        (internal if urlparse(u).netloc.endswith(host) else external).add(u)
    ld = []
    for s in soup.find_all("script", type="application/ld+json"):
        try:
            data = json.loads(s.string or "")
            graph = data.get("@graph", [data]) if isinstance(data, dict) else data
            ld += [",".join(t) if isinstance(t := n.get("@type"), list) else t for n in graph if isinstance(n, dict)]
        except Exception:
            ld.append("INVALID_JSON")
    main = soup.find("main") or soup.find("article") or soup.body
    text = main.get_text(" ", strip=True) if main else ""
    return {
        "title": title,
        "meta_description": g('meta[name="description"]'),
        "robots": g('meta[name="robots"]'),
        "canonical": g('link[rel="canonical"]', "href"),
        "og_title": g('meta[property="og:title"]'),
        **hs,
        "images": imgs,
        "img_missing_alt": sum(1 for i in imgs if not (i["alt"] or "").strip()),
        "internal_links": sorted(internal),
        "external_links": sorted(external),
        "jsonld_types": ld,
        "words": len(re.findall(r"\w+", text)),
        "tel_links": [a["href"] for a in soup.select('a[href^="tel:"]')],
        "calendly": bool(re.search(r"calendly\.com", html)),
    }


def issues_for(r):
    out = []
    add = lambda prio, msg, fix: out.append((prio, msg, fix))
    if r["status"] != 200:
        add("P1", f"HTTP {r['status']}", "Corriger ou rediriger")
        return out
    t = r.get("title") or ""
    if not t:
        add("P1", "Titre absent", "Définir un titre SEO Yoast")
    elif len(t) > 65:
        add("P3", f"Titre long ({len(t)} car.)", "Raccourcir à ~50-60 car.")
    elif len(t) < 25:
        add("P2", f"Titre court/peu descriptif ({len(t)} car.)", "Titre SEO descriptif")
    if re.match(r"^(Home|About|Home 2|sdfqsdf)\b", t):
        add("P1", f"Titre générique « {t} »", "Titre SEO spécifique")
    md = r.get("meta_description") or ""
    if not md:
        add("P2", "Méta-description absente", "Rédiger 120-155 car.")
    elif len(md) > 160:
        add("P3", f"Méta-description longue ({len(md)})", "Raccourcir")
    if len(r["h1"]) == 0:
        add("P2", "Aucun H1", "Ajouter un H1 unique")
    elif len(r["h1"]) > 1:
        add("P3", f"{len(r['h1'])} H1", "Un seul H1")
    rob = (r.get("robots") or "").lower()
    if "noindex" in rob:
        add("INFO", "noindex", "Vérifier que c'est voulu")
    can = r.get("canonical")
    if can and can.rstrip("/") != r["final_url"].rstrip("/"):
        add("P2", f"Canonical différent : {can}", "Vérifier")
    if r["redirects"]:
        add("INFO", "Redirigée : " + " > ".join(r["redirects"]), "Mettre à jour les liens")
    if r["img_missing_alt"]:
        add("P3", f"{r['img_missing_alt']} image(s) sans ALT", "ALT descriptif")
    if r["words"] < 150 and r.get("type") in ("page", "post"):
        add("P2", f"Contenu faible ({r['words']} mots)", "Enrichir, fusionner ou noindex")
    if r["html_kb"] > 300:
        add("P3", f"HTML lourd ({r['html_kb']} Ko)", "Alléger")
    return out


def main(site):
    root = Path(__file__).resolve().parent.parent
    out = root / "sites" / site / "audit" / dt.date.today().isoformat()
    out.mkdir(parents=True, exist_ok=True)
    wp = WPClient(site)
    host = urlparse(wp.base).netloc

    items = []
    for kind, ep in [("page", "pages"), ("post", "posts"), ("category", "categories"), ("tag", "tags")]:
        for o in wp.get_all(ep, {"_fields": "id,link,slug,status,count,modified,parent,title"}):
            items.append({"type": kind, "id": o["id"], "url": o["link"], "slug": o["slug"],
                          "count": o.get("count"), "modified": o.get("modified"),
                          "wp_title": (o.get("title") or {}).get("rendered") if isinstance(o.get("title"), dict) else None})

    s = requests.Session()

    def work(it):
        try:
            r, chain = fetch(s, it["url"])
            it.update(status=r.status_code, final_url=r.url, redirects=chain,
                      html_kb=round(len(r.content) / 1024), litespeed=r.headers.get("x-litespeed-cache"))
            if r.status_code == 200 and "html" in r.headers.get("content-type", ""):
                it.update(parse_page(r.url, r.text, host))
        except Exception as e:
            it.update(status="ERR", error=str(e)[:200], redirects=[], html_kb=0)
        it.setdefault("h1", []); it.setdefault("img_missing_alt", 0); it.setdefault("words", 0)
        it["issues"] = issues_for(it)
        return it

    with ThreadPoolExecutor(max_workers=4) as ex:
        results = list(ex.map(work, items))

    # Liens internes cassés (vérification HEAD des cibles uniques)
    known = {r["final_url"].rstrip("/") for r in results if r.get("final_url")}
    targets = {u for r in results for u in r.get("internal_links", [])
               if "/wp-content/" not in u and u.rstrip("/") not in known and "?" not in u}
    broken = {}
    def head(u):
        try:
            x = s.head(u, timeout=20, allow_redirects=False, headers={"User-Agent": UA})
            return u, x.status_code, x.headers.get("location")
        except Exception as e:
            return u, "ERR", str(e)[:80]
    with ThreadPoolExecutor(max_workers=4) as ex:
        for u, code, loc in ex.map(head, sorted(targets)):
            if code != 200:
                broken[u] = (code, loc)
    inbound = collections.defaultdict(list)
    for r in results:
        for u in r.get("internal_links", []):
            inbound[u.rstrip("/")].append(r["url"])
    for r in results:
        r["inbound_count"] = len(inbound.get(r["url"].rstrip("/"), []))

    # Doublons de titres / descriptions
    dup_t = collections.Counter(r.get("title") for r in results if r.get("title"))
    dup_d = collections.Counter(r.get("meta_description") for r in results if r.get("meta_description"))
    for r in results:
        if r.get("title") and dup_t[r["title"]] > 1:
            r["issues"].append(("P2", f"Titre dupliqué ({dup_t[r['title']]}x)", "Titre unique"))
        if r.get("meta_description") and dup_d[r["meta_description"]] > 1:
            r["issues"].append(("P3", "Méta-description dupliquée", "Description unique"))

    (out / "urls.json").write_text(json.dumps({"results": results, "broken_internal": broken},
                                              ensure_ascii=False, indent=1))
    with open(out / "urls.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["type", "id", "url", "status", "title", "len_title", "meta_description",
                    "robots", "canonical", "h1", "h1_count", "words", "img", "img_no_alt",
                    "inbound", "jsonld", "issues"])
        for r in results:
            w.writerow([r["type"], r["id"], r["url"], r["status"], r.get("title"), len(r.get("title") or ""),
                        r.get("meta_description"), r.get("robots"), r.get("canonical"),
                        " | ".join(r["h1"]), len(r["h1"]), r["words"], len(r.get("images", [])),
                        r["img_missing_alt"], r["inbound_count"], ",".join(map(str, r.get("jsonld_types", []))),
                        " ; ".join(f"[{p}] {m}" for p, m, _ in r["issues"])])
    print(f"OK {len(results)} URLs, {len(broken)} liens internes non-200 -> {out}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "sabinekouli.com")
