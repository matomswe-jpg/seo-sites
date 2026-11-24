# sabinekouli.com : état initial SEO (24/11/2026)

Audit **en lecture seule** sans authentification : API REST publique et HTML publié, après le cache LiteSpeed.
Données brutes : `audit/2026-11-24/urls.json`, `urls.csv`, `issues.md` (475 lignes, une par anomalie).

## Inventaire

| Type | Nombre | Remarque |
|---|---|---|
| Pages publiées | 46 | toutes en `index, follow` |
| Articles | 137 | toutes en `index, follow` |
| Catégories | 10 | indexées |
| Étiquettes | 76 (65 dans le sitemap) | 57 n'ont qu'un article, 11 n'en ont aucun |
| Médias | 557 | les pages de fichier joint redirigent en 301 vers le fichier (réglage Yoast correct) |
| Sitemaps Yoast | post, page, category, post_tag, author | |
| Auteurs | 2 archives d'auteur dans le sitemap | ⚠️ les slugs ressemblent à des identifiants de connexion |

## Constats globaux

| Point | Résultat |
|---|---|
| HTTPS, www vers sans www | OK (301) |
| robots.txt | OK, géré par Yoast, aucun blocage, sitemap déclaré |
| Méta-descriptions | **0 sur 269 URL** |
| Titres SEO | tous au modèle par défaut `%%title%% - Sabine Kouli`. 29 articles dépassent 65 caractères |
| H1 | accueil sans H1 (premier titre : un H3 « Sabine Kouli »). 3 articles et 11 étiquettes ont 2 H1 (thème) |
| Canonical | présent partout et auto-référent, aucune anomalie |
| noindex | aucune URL |
| Liens internes cassés | 2 en 404 : `/pedagogies-vocales/gospel-negro-spirituals/` (depuis la bio) et un lien « bali & thailande » mal formé dans un article |
| Liens vers les pages de fichier joint | 86 liens internes vers d'anciennes pages de pièce jointe (301 vers les images) : sans gravité |
| JSON-LD (Yoast) | WebPage/Article, BreadcrumbList, WebSite, **Organization** (nom et logo, sans adresse ni téléphone ni sameAs). Person seulement sur les articles, en tant qu'auteur |
| NAP | **aucun téléphone, aucun lien `tel:`, aucune adresse** sur le site. « Caluire 69300 » une seule fois (page coaching) |
| Calendly | présent sur la page coaching uniquement (bas de page) |
| Poids HTML | 106 à 143 Ko par page, cache LiteSpeed actif (UCSS, JS différé, lazy-load) |
| Page de stage `/stage-de-technique-vocale/` (ID 3669) | **aucun lien interne entrant** (absente des menus) |
| Liens de pied de page | 372 liens vers `sabinekouli.wordpress.com` et 268 vers `journeefemmeafricaine.com` (widgets répétés) : à vérifier |

## Pages stratégiques

| URL | ID | Titre actuel | Méta | H1 | Mots (contenu) | Observations |
|---|---|---|---|---|---|---|
| `/` | 12 | Home - Sabine Kouli | — | **aucun** | contenu construit par le thème | H1 et textes gérés dans les options du thème |
| `/pedagogies-vocales/cours-et-coaching-vocal/` | 553 | Cours et coaching vocal individuel - Sabine Kouli | — | oui | 407 | « Lyon » 0 fois, « Caluire » 1 fois, Calendly présent, pas de FAQ ni de tarifs |
| `/pedagogies-vocales/` | 269 | Pédagogie Vocale - Sabine Kouli | — | oui | 146 | contenu léger |
| `/stage-de-technique-vocale/` | 3669 | Stage de technique vocale - Sabine Kouli | — | oui | 140 | page orpheline |
| `/infos-pratiques/contact/` | 792 | Contact - Sabine Kouli | — | oui | 39 | formulaire seul, sans NAP |
| `/sabine-kouli-chanteuse-gospel/` | 97 | **Sabine Kouli - Sabine Kouli** | — | oui | 772 | 4 images sur 5 sans ALT, lien en 404 |
| `/about/` | 1 | About | — | oui | ~0 (texte par défaut) | aucun lien entrant, indexable |
| `/home-2/` | 706 | Home 2 | — | oui | 0 | vide, aucun lien entrant, indexable |
| `/sdfqsdf/` | 900 | sdfqsdf | — | oui | 1 | page de test, aucun lien entrant, indexable |
| `/infos-pratiques/` | 692 | **Pratik** | — | oui | 16 | titre peu explicite |

## Comparaison avec le plan SEO du 13/11/2026

| # | Constat du plan | Vérifié le 24/11 | Commentaire |
|---|---|---|---|
| 1 | Aucune méta-description | ✅ confirmé, et généralisé à 100 % des URL | |
| 2 | Titre de l'accueil « Home – Sabine Kouli » | ✅ confirmé | |
| 3 | Pas de H1 sur l'accueil | ✅ confirmé | dépend du thème, pas de l'éditeur |
| 4 | `/sdfqsdf/`, `/home-2/`, `/about/` indexables | ✅ confirmé | aucun lien interne entrant. Indexation Google réelle à confirmer dans Search Console |
| 5 | Schema limité à « Organization » sans adresse ni téléphone | ✅ confirmé | voir la nuance sur le type ProfessionalService dans le plan d'action |
| 6 | NAP absent, aucun téléphone | ✅ confirmé | |
| 7 | Page coaching mal ciblée (Lyon 0 fois) | ✅ confirmé | 407 mots de contenu propre (le plan en estimait environ 450) |
| 8 | Titre de la bio en doublon | ✅ confirmé | |
| 9 | « Environ 90 étiquettes indexées » | ⚠️ **76 étiquettes**, dont 65 dans le sitemap | le chiffre du plan est surestimé, la recommandation reste valable |
| 10 | Activité de coach peu visible | ✅ cohérent | décision éditoriale et menu, à valider |
| 11 | Bio : 4 images sur 5 sans ALT | ✅ confirmé | |
| — | Calendly présent | ✅ uniquement sur la page coaching | |
| Nouveau | 2 liens internes en 404 | non signalé dans le plan | |
| Nouveau | Page de stage orpheline | non signalé | |
| Nouveau | Archives d'auteur exposant des identifiants | non signalé | sécurité et contenu dupliqué |
| Nouveau | Méta « 25 ans » dans le texte d'accueil proposé | à valider | chiffre non confirmé |
| Nouveau | Tarif « moyenne Superprof 37 €/h » | ne pas reprendre | aucun tarif publié sans votre confirmation |

## Non mesurable sans accès supplémentaire

- Indexation réelle, requêtes et positions : **Google Search Console** (accès à donner, ou exports CSV).
- Contenu brut des pages (blocs) et métadonnées Yoast stockées : Application Password.
- Core Web Vitals réels : données CrUX ou PageSpeed (trafic peut-être insuffisant pour CrUX).
- Fiche Google Business Profile : aucun accès.
