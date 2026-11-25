# sabinekouli.com : journal des changements

Une entrée par intervention en production, **après** validation explicite.

| Date | Page / élément (ID, URL) | Problème initial | Changement effectué | Raison SEO | Contrôle (API + HTML publié) | Retour arrière | Validé par |
|---|---|---|---|---|---|---|---|
| 2026-11-24 | — | — | Aucun changement. Audit en lecture seule et préparation | — | — | — | — |
| 2026-11-25 | Wordfence > Pare-feu > Protection anti force brute | Mots de passe d'application désactivés (option Wordfence) | Case « Désactiver les mots de passe des applications WordPress » décochée, par Sabine | Prérequis d'accès API (pas un changement SEO) | `/wp-json/` expose `application-passwords` ✅ | Recocher la case | Sabine |
| 2026-11-25 | Comptes | — | Création du compte `seo-technique-site` (Éditeur) et d'un mot de passe d'application `claude-code-seo`, par Sabine | Accès technique dédié et révocable | Compte créé ✅ | Révoquer le mot de passe d'application ou supprimer le compte | Sabine |
| 2026-11-25 | `.htaccess` (via Yoast > Outils > Éditeur de fichiers) | En-tête Authorization non transmis à PHP | Ajout en tête : `SetEnvIf Authorization "(.*)" HTTP_AUTHORIZATION=$1`, puis un bloc `RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]`, par Sabine | Prérequis d'accès API | Site en 200 ✅ ; authentification toujours refusée (`rest_not_logged_in`, y compris depuis le Mac de Sabine) ❌ | Recoller la sauvegarde du .htaccess d'origine (Notes de Sabine) | Sabine |
