#!/usr/bin/env python3
"""Sauvegarde de CONTENU (lecture seule) d'un site WordPress, via l'API REST publique.

Usage : python3 scripts/export_public.py sabinekouli.com [--no-media]

Exporte dans sites/<site>/backups/<date>/ :
  rest/*.json     pages, articles, catégories, étiquettes, médias (contenu rendu + yoast_head_json)
  html/           HTML publié de chaque page et article (état SEO réel)
  seo/            robots.txt et sitemaps
  media/          fichiers originaux de la médiathèque (sauf --no-media)
  MANIFEST.md     contenu exact et limites

Ce N'EST PAS une sauvegarde complète restaurable : la base de données (réglages,
métadonnées Yoast stockées, utilisateurs, menus, widgets, formulaires, contenus
non publiés), le thème, les extensions et wp-config.php exigent un accès serveur
(sauvegarde OVH, UpdraftPlus ou WP-CLI).
"""
import datetime as dt, json, re, sys, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).parent))
from wp_client import WPClient  # noqa: E402


def main(site, media=True):
    wp = WPClient(site)
    out = Path(__file__).resolve().parent.parent / "sites" / site / "backups" / dt.date.today().isoformat()
    for d in ("rest", "html", "seo", "media"):
        (out / d).mkdir(parents=True, exist_ok=True)
    counts = {}
    for ep in ("pages", "posts", "categories", "tags", "media", "comments"):
        data = wp.get_all(ep)
        (out / "rest" / f"{ep}.json").write_text(json.dumps(data, ensure_ascii=False, indent=1))
        counts[ep] = len(data)
    (out / "rest" / "site.json").write_text(json.dumps(wp.get("").json(), ensure_ascii=False)[:2_000_000])

    for f in ("robots.txt", "sitemap_index.xml"):
        r = wp.s.get(f"{wp.base}/{f}", timeout=30)
        (out / "seo" / f).write_bytes(r.content)
        for loc in re.findall(r"<loc>([^<]+)</loc>", r.text) if f.endswith(".xml") else []:
            (out / "seo" / loc.rsplit("/", 1)[-1]).write_bytes(wp.s.get(loc, timeout=30).content)

    urls = [o["link"] for ep in ("pages", "posts")
            for o in json.loads((out / "rest" / f"{ep}.json").read_text())]

    def save_html(u):
        name = (urlparse(u).path.strip("/").replace("/", "__") or "accueil") + ".html"
        (out / "html" / name).write_bytes(wp.s.get(u, timeout=40).content)
    with ThreadPoolExecutor(4) as ex:
        list(ex.map(save_html, urls))

    failed = []
    if media:
        items = json.loads((out / "rest" / "media.json").read_text())

        def dl(m):
            u = m["source_url"]
            p = out / "media" / urlparse(u).path.split("/wp-content/uploads/")[-1]
            p.parent.mkdir(parents=True, exist_ok=True)
            if p.exists():
                return
            for _ in range(3):
                try:
                    r = wp.s.get(u, timeout=120)
                    if r.ok:
                        p.write_bytes(r.content); return
                except Exception:
                    time.sleep(2)
            failed.append(u)
        with ThreadPoolExecutor(4) as ex:
            list(ex.map(dl, items))

    (out / "MANIFEST.md").write_text(f"""# Sauvegarde de contenu public : {site}

Date : {dt.datetime.now().isoformat(timespec='minutes')}
Méthode : API REST publique + HTML publié (lecture seule, aucun identifiant).

| Élément | Nombre |
|---|---|
""" + "\n".join(f"| {k} | {v} |" for k, v in counts.items()) + f"""
| HTML publiés | {len(urls)} |
| Médias en échec | {len(failed)} |

## Contenu
- `rest/` : JSON complet de l'API (contenu HTML rendu, extraits, dates, slugs, parents, médias avec ALT, `yoast_head_json`).
- `html/` : pages telles que servies (titres, méta, schema réels à cette date).
- `seo/` : robots.txt et sitemaps Yoast.
- `media/` : fichiers originaux, arborescence `uploads/` conservée.

## Limites : ceci n'est PAS une sauvegarde restaurable du site
Non inclus (accès serveur requis) : base de données, contenus « source » des blocs, brouillons et pages privées,
réglages WordPress et Yoast, métadonnées SEO stockées, menus, widgets, utilisateurs, formulaires,
thème, extensions, `wp-config.php`, `.htaccess`, tailles d'images générées.
Utilité : archive de référence, restauration manuelle de textes et d'images, preuve de l'état SEO initial.

Médias en échec :
""" + "\n".join(f"- {u}" for u in failed) + "\n")
    print(counts, "html", len(urls), "media_failed", len(failed), "->", out)


if __name__ == "__main__":
    main(sys.argv[1], media="--no-media" not in sys.argv)
