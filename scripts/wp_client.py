"""Client WordPress REST minimal, isolé par site.

Configuration : sites/<domaine>/.env.local (jamais versionné), variables :
  WP_BASE_URL, WP_USER, WP_APP_PASSWORD
Les variables d'environnement du processus ont priorité (utile en CI/cloud).

Sécurité :
- le mot de passe n'est jamais affiché, journalisé ni écrit sur disque ;
- les écritures exigent allow_write=True ET un appel explicite à write() ;
- chaque site a son propre fichier : aucun partage d'identifiants entre sites.
"""
import os
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
UA = "SEO-Maintenance/1.0 (+read-only by default)"


def load_env(site):
    env = {}
    f = ROOT / "sites" / site / ".env.local"
    if f.exists():
        for line in f.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    for k in ("WP_BASE_URL", "WP_USER", "WP_APP_PASSWORD"):
        if os.environ.get(k):
            env[k] = os.environ[k]
    return env


class WPClient:
    def __init__(self, site, allow_write=False):
        env = load_env(site)
        self.site = site
        self.base = env.get("WP_BASE_URL", f"https://{site}").rstrip("/")
        self.s = requests.Session()
        self.s.headers["User-Agent"] = UA
        self.authenticated = bool(env.get("WP_USER") and env.get("WP_APP_PASSWORD"))
        if self.authenticated:
            self.s.auth = (env["WP_USER"], env["WP_APP_PASSWORD"])
        self.allow_write = allow_write

    def __repr__(self):  # jamais de secret dans les représentations
        return f"<WPClient {self.base} auth={'yes' if self.authenticated else 'no'}>"

    def get(self, path, params=None):
        url = path if path.startswith("http") else f"{self.base}/wp-json/{path.lstrip('/')}"
        return self.s.get(url, params=params, timeout=30)

    def get_all(self, endpoint, params=None):
        params = dict(params or {}, per_page=100, page=1)
        out = []
        while True:
            r = self.get(f"wp/v2/{endpoint}", params)
            if r.status_code != 200:
                break
            out += r.json()
            if params["page"] >= int(r.headers.get("X-WP-TotalPages", 1)):
                break
            params["page"] += 1
        return out

    def write(self, method, path, json=None):
        """Écriture : réservée aux scripts d'exécution validés (niveau 3)."""
        if not (self.allow_write and self.authenticated):
            raise PermissionError("Écriture refusée : client en lecture seule ou non authentifié.")
        url = f"{self.base}/wp-json/{path.lstrip('/')}"
        return self.s.request(method, url, json=json, timeout=60)
