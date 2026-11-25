# Connexion technique à WordPress

## 1. Méthodes possibles et choix retenu

| Méthode | Fiabilité | Sécurité | Usage retenu |
|---|---|---|---|
| **API Abilities** (`wp-abilities/v1`, WordPress 6.9 ou plus) | Élevée, native | Permissions WordPress et Yoast appliquées | **1er choix** pour les métadonnées Yoast (`yoast-seo/get-post-seo-data`, `yoast-seo/update-post-seo-data`), si ces capacités sont exposées |
| **API REST WordPress** (`wp/v2`) et Application Password | Élevée | Révocable, propre à un compte, sans mot de passe principal | **Méthode principale** : contenus, brouillons, médias (texte ALT), étiquettes |
| API REST Yoast (`yoast/v1`) | Lecture fiable (`get_head`) | — | Contrôle du `<head>` réellement généré. Ne sert pas d'API d'écriture officielle |
| WP-CLI par SSH | Très élevée | Clé SSH, accès complet au serveur | **Dernier recours** : réglages Yoast globaux, export de la base, opérations hors API |
| Serveur MCP sur mesure | — | Surface d'attaque en plus | **Non retenu** : les solutions natives suffisent |

## 2. Procédure commune à chaque site

1. L'administrateur crée un **utilisateur technique dédié** (par exemple `seo-technique`), avec une adresse e-mail que vous contrôlez.
   - Rôle recommandé : **Éditeur**. Il permet de modifier pages et articles, de créer des brouillons, de gérer les médias et les étiquettes, et Yoast lui donne `wpseo_edit_advanced_metadata` et `wpseo_bulk_edit`.
   - Pas de rôle **Administrateur**.
   - Les réglages globaux de Yoast (archives d'étiquettes, archives d'auteur, représentation du site) demandent `wpseo_manage_options`. Deux options : vous les faites vous-même en suivant mes instructions pas à pas (recommandé), ou vous accordez **temporairement** le rôle « Gestionnaire SEO » de Yoast, puis vous le retirez.
2. **Connecté en tant que cet utilisateur technique**, allez dans *Utilisateurs > Profil > Mots de passe d'application*, saisissez le nom `claude-code-seo`, puis cliquez sur « Ajouter ».
3. Copiez le mot de passe affiché : il ne sera plus jamais montré.
4. Sur la machine qui exécute Claude Code, créez `sites/<domaine>/.env.local` à partir de `.env.example` et collez-y l'identifiant et le mot de passe d'application. **Ne collez pas ce mot de passe dans la conversation.**
5. Lancez `python3 scripts/check_connection.py <domaine>` pour vérifier les capacités.
6. Révocation : *Profil > Mots de passe d'application > Révoquer*, efficace immédiatement.

> Session cloud Claude Code : le conteneur est éphémère. Le fichier `.env.local` disparaît en fin de session, ce qui est voulu. Pour un usage durable, gardez-le sur votre ordinateur (Claude Code en local) ou enregistrez-le comme *secret d'environnement* dans les réglages de l'environnement cloud, jamais dans Git.

## 3. sabinekouli.com : constats du 24/11/2026

| Élément | Constat | Source |
|---|---|---|
| WordPress | 7.1.5 | meta generator |
| PHP | 8.4 | en-tête `x-powered-by` |
| Yoast SEO | 28.9 (« Stable tag » du readme public) | readme.txt |
| LiteSpeed Cache | actif (en-têtes `x-litespeed-tag`, JS différé, UCSS) | en-têtes HTTP |
| Thème | rock-singer-pro-premium | HTML |
| Autres extensions | Wordfence 9.1.1, Contact Form 7 6.2.6, Complianz 7.5.7, PixelYourSite 11.4.7, Akismet | readme et namespaces REST |
| Hébergement | OVH (AS16276), hébergement mutualisé probable, serveur Apache | IP 164.132.235.17 |
| API REST | ouverte (HTTP 200) | `/wp-json/` |
| API Abilities | **présente** (`wp-abilities/v1`), la liste demande une authentification | `/wp-json/wp-abilities/v1/abilities`, réponse 401 |
| API Yoast | présente (`yoast/v1`), `get_head` lisible publiquement | |
| **Application Passwords** | **probablement désactivées** : la clé `authentication` de `/wp-json/` est vide | `/wp-json/` |
| WP-CLI / SSH | non vérifiable sans identifiants. Les offres OVH « Pro » et supérieures proposent SSH, et WP-CLI y est installé | à confirmer |
| XML-RPC | désactivé (405), c'est bien | |
| Indexables Yoast | `yoast_head_json` présent et cohérent sur toutes les URL testées. L'état complet (fin de l'indexation) se vérifie en admin : *Yoast SEO > Outils > Optimiser les données SEO* | |

### Étapes à faire de votre côté (environ 10 minutes)

1. **Réactiver les Application Passwords dans Wordfence.**
   *Wordfence > Login Security > Paramètres* : décochez « Disable WordPress application passwords », puis enregistrez.
   Si l'option est déjà décochée, une autre extension ou un réglage d'hébergement les bloque : signalez-le-moi.
2. **Créer l'utilisateur technique.**
   *Utilisateurs > Ajouter*. Identifiant : `seo-technique` (jamais `admin`). Rôle : **Éditeur**. Pas de notification d'e-mail nécessaire.
3. **Si Wordfence impose la double authentification (2FA)** aux éditeurs : les Application Passwords restent compatibles avec l'API REST, donc rien à changer.
4. **Créer le mot de passe d'application** depuis le profil de `seo-technique`, sous le nom `claude-code-seo`.
5. Remplir `sites/sabinekouli.com/.env.local` avec `WP_USER=seo-technique` et `WP_APP_PASSWORD=...`.
6. **Sauvegarde :** dans l'espace client OVH, vérifiez que les sauvegardes automatiques de l'hébergement et de la base de données sont actives, avec leur date. Faites aussi une sauvegarde manuelle avant la première modification. Si vous voulez une restauration indépendante d'OVH : UpdraftPlus (gratuit) vers Google Drive.
7. **Staging :** OVH mutualisé ne propose pas de préproduction en un clic. Option sûre : tout préparer en **brouillon** (prévisualisation privée), modifier une page à la fois avec export de l'état initial, et ne toucher aux réglages globaux qu'après une sauvegarde manuelle.

### Après la connexion, je vérifierai

- l'authentification et le rôle effectif ;
- `wpseo_edit_advanced_metadata`, `edit_others_pages`, `edit_published_pages`, `upload_files`, `manage_categories` ;
- la liste réelle des abilities, et si `yoast-seo/get-post-seo-data` et `yoast-seo/update-post-seo-data` en font partie ;
- les champs `meta` exposés en écriture par l'API REST, comme solution de repli si les abilities Yoast sont absentes.

## 4. Limites connues

- L'API REST de Yoast permet de **lire** (`yoast_head_json`, `get_head`), mais elle ne garantit pas l'**écriture** des champs `_yoast_wpseo_title`, `_yoast_wpseo_metadesc` et `_yoast_wpseo_meta-robots-noindex`. Ces métadonnées ne sont pas déclarées dans `register_meta` pour la REST par défaut.
  Ordre de préférence pour écrire : (1) l'ability `yoast-seo/update-post-seo-data` ; (2) WP-CLI `wp post meta update` suivi de la reconstruction des indexables ; (3) la saisie manuelle guidée dans l'éditeur.
- Les réglages globaux de Yoast (taxonomies, archives, représentation du site) passent par l'administration ou par WP-CLI (`wp option`), avec `wpseo_manage_options`.
- Les redirections 301 se font avec Yoast Premium, l'extension « Redirection », ou un fichier `.htaccess` (OVH/Apache). Chacune demande votre accord et n'est pas faisable avec le rôle Éditeur.
- Google Business Profile : aucun accès depuis WordPress. C'est une mission séparée, avec des textes préparés pour validation.

## 5. Accès aux 4 sites (mise à jour du 24/11/2026)

Constat commun : sur sabinekouli.com, lajaama.fr, absolutegospel.fr et baobabetcie.fr, **Wordfence est actif** et les Application Passwords **ne sont pas exposées**. La même procédure s'applique **à chaque site, séparément**.

### Sur chaque site (environ 5 minutes par site, avec un compte administrateur)

1. *Wordfence > Login Security > Paramètres* : décochez **« Disable WordPress application passwords »**, puis enregistrez.
2. *Utilisateurs > Ajouter* : identifiant `seo-technique`, une adresse e-mail que vous contrôlez, rôle **Éditeur**.
3. Déconnectez-vous, puis connectez-vous en tant que `seo-technique`. Allez dans *Profil > Mots de passe d'application*, saisissez le nom `claude-code-seo`, cliquez sur **Ajouter**, puis copiez le mot de passe affiché (il ne réapparaît plus).
4. **Ne collez jamais ce mot de passe dans la conversation.**

Les réglages Yoast globaux et l'installation d'extensions demandent les droits administrateur. Ces opérations restent faites par vous, guidées pas à pas, ou par un rôle accordé temporairement.

### Transmission sécurisée (session cloud Claude Code)

Je vous affiche un **formulaire sécurisé** par site (un hôte = un secret) :
- vous saisissez l'identifiant `seo-technique` et le mot de passe d'application ;
- le secret est enregistré dans les *network secrets* de votre environnement cloud. Le proxy l'ajoute uniquement aux requêtes vers **cet** hôte. Le secret n'apparaît jamais dans la conversation, les fichiers ou Git ;
- `sites/<site>/.env.local` contient alors seulement `WP_AUTH_MODE=proxy` (aucun secret) ;
- cet environnement est votre environnement **Default** (personnel) : le secret servira aussi à vos futures sessions cloud, ce qui évite de recommencer à chaque fois ;
- pour révoquer : supprimer le mot de passe d'application dans WordPress, effet immédiat. Le secret peut aussi être retiré dans les réglages de l'environnement.

Alternative en local (Claude Code sur votre ordinateur) : `sites/<site>/.env.local` avec `WP_USER` et `WP_APP_PASSWORD`, fichier ignoré par Git.

### Vérification

`python3 scripts/check_connection.py <site>` : authentification, rôle, `wpseo_edit_advanced_metadata`, abilities `yoast-seo/*`, lecture en mode édition.

## 6. sabinekouli.com : diagnostic d'accès API (25/11/2026)

Résultat : **l'authentification par mot de passe d'application échoue depuis l'extérieur**. Toute requête authentifiée répond `401 rest_not_logged_in`, y compris depuis le Mac de Sabine. Un identifiant volontairement faux donne la même réponse : WordPress ne lit pas l'en-tête.

Vérifié et écarté :
- mots de passe d'application : réactivés (option Wordfence « Désactiver les mots de passe des applications WordPress » décochée), exposés dans `/wp-json/` ✅ ;
- `.htaccess` : directives SetEnvIf et RewriteRule (version OVH) en tête de fichier ;
- Santé du site : « L'entête d'autorisation fonctionne comme prévu » ✅. Ce test vérifie seulement une requête interne du serveur vers lui-même ;
- extensions désactivées une à une ou par groupe, sans effet : PixelYourSite, Maintenance, Disable Comments, LiteSpeed Cache, Wordfence, Akismet, Complianz, Contact Form 7, Duplicate Page, Post Type Switcher, Quick Featured Images, WordPress Importer, Yoast SEO ;
- pare-feu applicatif OVH (mod_security) désactivé pendant 5 minutes : sans effet, puis remis sur « sécurité ».

Hypothèses restantes : le thème (rock-singer-pro, non testé), ou un traitement des requêtes externes par l'infrastructure OVH.

Incident : après de nombreuses requêtes de test avec un faux identifiant, l'adresse IP de la session cloud a été bloquée (403 Apache sur tout le site). Le site restait accessible normalement aux visiteurs (vérifié par Sabine en navigation privée). **Ne plus envoyer de requêtes avec de faux identifiants.**

Solution de repli recommandée : **WP-CLI par SSH** (offre OVH Pro, SSH actif), avec Claude Code exécuté en local sur le Mac de Sabine.
