# sabinekouli.com : résultats des contrôles

## Grille de contrôle après chaque intervention

- [ ] `<title>` présent dans le HTML publié (après purge du cache LiteSpeed de l'URL)
- [ ] `meta name="description"` présente et identique à la valeur validée
- [ ] un seul H1, pertinent
- [ ] `link rel="canonical"` auto-référent
- [ ] `meta robots` conforme (index ou noindex voulu)
- [ ] redirections : code 301 et destination finale en 200
- [ ] JSON-LD : un seul graphe Yoast, `@id` stables, aucune erreur au Rich Results Test
- [ ] sitemap XML à jour (URL supprimées absentes, nouvelles URL publiées présentes)
- [ ] aucun nouveau lien interne en 404 (relancer `audit.py`)
- [ ] Calendly : le lien s'ouvre et le créneau est réservable
- [ ] affichage mobile et ordinateur (captures)
- [ ] en-tête `x-litespeed-cache: hit` au deuxième appel

## Historique

| Date | Contrôle | Résultat |
|---|---|---|
| 2026-11-24 | Audit initial, 269 URL, toutes en HTTP 200 | voir `seo-baseline.md` |
