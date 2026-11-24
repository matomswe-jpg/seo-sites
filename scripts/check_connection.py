#!/usr/bin/env python3
"""Diagnostic de connexion (lecture seule).

Usage : python3 scripts/check_connection.py sabinekouli.com

Vérifie : API REST, disponibilité des Application Passwords, authentification,
rôle et capacités de l'utilisateur technique (dont wpseo_edit_advanced_metadata),
API Abilities (WP >= 6.9) et capacités Yoast exposées, accès en édition à un
contenu (context=edit, sans écriture). N'affiche jamais de secret.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from wp_client import WPClient  # noqa: E402

WANTED_CAPS = ["edit_pages", "edit_others_pages", "edit_published_pages", "edit_posts",
               "edit_others_posts", "edit_published_posts", "manage_categories", "upload_files",
               "wpseo_edit_advanced_metadata", "wpseo_manage_options", "wpseo_bulk_edit",
               "manage_options", "delete_pages", "publish_pages", "list_users"]


def line(ok, label, detail=""):
    print(f"[{'OK ' if ok is True else '!! ' if ok is False else '-- '}] {label} {detail}")


def main(site):
    wp = WPClient(site)
    r = wp.get("")
    line(r.status_code == 200, "API REST", f"HTTP {r.status_code}")
    root = r.json() if r.ok else {}
    ns = root.get("namespaces", [])
    auth = root.get("authentication") or {}
    line("application-passwords" in auth, "Application Passwords disponibles",
         "" if auth else "(absent de /wp-json : désactivées, souvent par Wordfence ou un réglage de sécurité)")
    line("wp-abilities/v1" in ns, "API Abilities (wp-abilities/v1)")
    line("yoast/v1" in ns, "Yoast REST (yoast/v1)")

    if not wp.authenticated:
        line(None, "Authentification", "non configurée localement : test d'une éventuelle injection par le proxy")
    me = wp.get("wp/v2/users/me", {"context": "edit"})
    line(me.status_code == 200, "Authentification", f"HTTP {me.status_code}")
    if me.status_code != 200:
        print("    ", me.json().get("code"), "-", me.json().get("message"))
        return
    u = me.json()
    caps = u.get("capabilities", {})
    print(f"     utilisateur id={u.get('id')} rôles={u.get('roles')}")
    for c in WANTED_CAPS:
        line(bool(caps.get(c)), f"capacité {c}")
    if caps.get("manage_options"):
        line(False, "ATTENTION", "le compte technique est administrateur : droits supérieurs au besoin")

    ab = wp.get("wp-abilities/v1/abilities", {"per_page": 100})
    line(ab.status_code == 200, "Liste des abilities", f"HTTP {ab.status_code}")
    if ab.ok:
        names = sorted(a.get("name", "") for a in ab.json())
        for n in names:
            print("      -", n)
        for want in ("yoast-seo/get-post-seo-data", "yoast-seo/update-post-seo-data"):
            line(want in names, f"ability {want}")

    pg = wp.get("wp/v2/pages/553", {"context": "edit", "_fields": "id,link,status,meta,yoast_head_json"})
    line(pg.status_code == 200, "Lecture en édition page 553 (coaching)", f"HTTP {pg.status_code}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "sabinekouli.com")
