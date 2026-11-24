# Projet : maintenance SEO de sites WordPress

Instructions permanentes pour Claude Code. À relire au début de chaque intervention.

## Organisation

```
CLAUDE.md                 ce fichier (règles communes à tous les sites)
.env.example              modèle générique, sans secret
docs/wordpress-connection.md   procédure de connexion (commune + spécificités par site)
scripts/                  outils réutilisables (lecture seule par défaut)
  wp_client.py            client REST isolé par site ; écriture verrouillée par défaut
  check_connection.py     diagnostic d'accès et de capacités
  audit.py                audit SEO complet en lecture seule
  report_issues.py        tableau URL | Problème | Priorité | Correction | Action
sites/<domaine>/          UN DOSSIER PAR SITE, jamais de mélange
  .env.local              identifiants du site (ignoré par git, jamais affiché)
  .env.example            modèle du site
  site.md                 fiche d'identité : NAP, faits validés / à valider
  docs/seo-baseline.md    état initial
  docs/seo-action-plan.md plan d'intervention hiérarchisé
  docs/seo-change-log.md  historique des changements (avant / après / retour arrière)
  docs/seo-validation.md  résultats des contrôles
  audit/<date>/           sorties brutes des audits (urls.json, urls.csv, issues.md)
  backups/<date>/         états initiaux exportés avant modification
  drafts/                 textes et pages préparés, non publiés
```

## Règles impératives

1. **Trois niveaux.**
   - Niveau 1, analyse : lecture seule, sans limite.
   - Niveau 2, préparation : textes, scripts et brouillons locaux dans `drafts/`, sans rien publier.
   - Niveau 3, exécution : toute écriture en production (publication, suppression, redirection, réglage global d'indexation, plugin, thème, menu) exige une validation explicite, donnée dans la conversation en cours et pour ce changement précis.
2. **Isolation des sites.** Toujours passer le domaine aux scripts. Ne jamais réutiliser des identifiants, des contenus ou des conclusions d'un site sur un autre.
3. **Secrets.** Ne jamais afficher, journaliser, commiter ni copier dans un rapport le contenu de `.env.local`. Ne jamais demander le mot de passe principal WordPress. Seule une Application Password révocable, liée à un compte technique dédié, est utilisée.
4. **Permissions.** Ne jamais contourner une permission, ne jamais s'attribuer de droits et ne jamais créer de compte administrateur.
5. **Ordre de préférence des méthodes.** (a) API Abilities de WordPress (capacités `yoast-seo/*`) ; (b) API REST standard ; (c) WP-CLI par SSH, uniquement si (a) et (b) ne permettent pas l'opération. Pas de serveur MCP sur mesure si une solution native suffit.
6. **Avant chaque modification :** relever l'ID, l'URL, le statut, le titre SEO, la méta-description, la balise canonical, la directive robots et le JSON-LD. Vérifier que l'ID correspond à l'URL, puis enregistrer cet état dans `backups/`.
7. **Après chaque modification :** relire la donnée dans l'API, puis le HTML réellement publié (purger le cache LiteSpeed de l'URL si besoin). Consigner le résultat dans `seo-change-log.md` et `seo-validation.md`.
8. **Aucune information inventée :** ni tarif, ni avis, ni qualification, ni chiffre biographique, ni résultat. Tout fait non confirmé reste marqué `[À VALIDER]` dans `site.md`.
9. **Pas de modification massive** sans un essai préalable sur un seul élément, suivi d'un contrôle.
10. **Design, thème, menus et contenu artistique :** on n'y touche pas sans nécessité SEO démontrée et sans accord.
11. **Résultats :** ne jamais promettre une position Google. Ne présenter que des mesures réelles (Search Console, statistiques de la fiche Google).
12. **Désindexation :** passer par `noindex`, jamais par un blocage dans robots.txt.

## Commandes usuelles

```bash
python3 scripts/check_connection.py sabinekouli.com
python3 scripts/audit.py sabinekouli.com
python3 scripts/report_issues.py sabinekouli.com
```

Dépendances : Python 3.10 ou plus, `requests`, `beautifulsoup4`, `lxml`.
