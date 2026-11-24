#!/usr/bin/env python3
"""Génère le tableau URL | Problème | Priorité | Correction | Action à partir d'un audit.

Usage : python3 scripts/report_issues.py sabinekouli.com [AAAA-MM-JJ]
Sortie : sites/<domaine>/audit/<date>/issues.md et issues.csv
"""
import csv, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORDER = {"P1": 0, "P2": 1, "P3": 2, "INFO": 3}
ACTION = {"P1": "Niveau 3 – validation requise", "P2": "Niveau 2 – à préparer",
          "P3": "Niveau 2 – lot groupé", "INFO": "Niveau 1 – à vérifier"}


def main(site, date=None):
    base = ROOT / "sites" / site / "audit"
    d = base / (date or sorted(p.name for p in base.iterdir() if p.is_dir())[-1])
    data = json.loads((d / "urls.json").read_text())
    rows = []
    for r in data["results"]:
        for prio, msg, fix in r["issues"]:
            rows.append((ORDER[prio], r["type"], r["url"], msg, prio, fix, ACTION[prio]))
    for u, (code, loc) in data["broken_internal"].items():
        if code == 404 or code == "ERR":
            src = [r["url"] for r in data["results"] if u in r.get("internal_links", [])]
            rows.append((0, "lien", u, f"Lien interne en {code} (depuis {', '.join(src)})", "P1",
                         "Corriger le lien source", ACTION["P1"]))
    rows.sort()
    with open(d / "issues.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["type", "URL", "Problème constaté", "Priorité", "Correction recommandée", "Action à réaliser"])
        w.writerows(r[1:] for r in rows)
    md = ["| Type | URL | Problème constaté | Priorité | Correction recommandée | Action |", "|---|---|---|---|---|---|"]
    md += [f"| {t} | {u.replace('https://' + site, '') or '/'} | {m.replace('|', '/')} | {p} | {fx} | {a} |"
           for _, t, u, m, p, fx, a in rows]
    (d / "issues.md").write_text("\n".join(md) + "\n")
    print(f"{len(rows)} lignes -> {d}/issues.md")


if __name__ == "__main__":
    main(*sys.argv[1:] or ["sabinekouli.com"])
