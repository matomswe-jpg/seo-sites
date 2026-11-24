# Intégration de « Il était une voix » : comparaison et recommandation

## Contraintes techniques vérifiées

| Question | Réponse | Source |
|---|---|---|
| Redirection 301 depuis le blog Wix ? | **Impossible** sur une adresse gratuite `wixsite.com`. Il faut un forfait Premium **et** un domaine connecté. Le gestionnaire de redirections Wix accepte alors une URL externe | [Wix : redirection 301 d'une page](https://support.wix.com/en/article/setting-up-a-301-redirect-for-a-page-on-your-site), [transfert de domaine](https://support.wix.com/en/article/setting-up-a-301-redirect-from-one-domain-to-another) |
| Canonical vers une URL externe ? | **Possible** article par article : *Blog > Modifier > SEO > Avancé > Balises supplémentaires > canonical*. Disponibilité sur le forfait gratuit à vérifier dans votre interface | [Wix Blog : réglages SEO](https://support.wix.com/en/article/wix-blog-customizing-your-blogs-seo-settings) |
| noindex d'un article Wix ? | Possible dans les réglages SEO de l'article (« Laisser les moteurs indexer cette page ») | idem |
| Export Wix vers WordPress | Wix n'a pas d'export WordPress officiel. Le flux RSS (`/blog-feed.xml`) ne contient que les 20 derniers articles et le texte tronqué. **Méthode retenue : notre propre extraction**, déjà faite (`wix/content/*.md`, 52 sur 52, avec dates et images) | [WPBeginner](https://www.wpbeginner.com/wp-tutorials/how-to-properly-switch-from-wix-to-wordpress-step-by-step/), [Blog Porter](https://wordpress.org/plugins/blog-porter/) |
| Droits sur les images | 69 images hébergées sur `wixstatic.com`. Origine inconnue (photos personnelles ou banques d'images Wix ?) | **à confirmer par vous** |

## Comparaison

| Critère | Option A : Wix conservé + page passerelle | Option B : migration progressive vers WordPress |
|---|---|---|
| Intérêt SEO | faible. Les liens sortants n'apportent rien à sabinekouli.com, et le blog Wix est largement en noindex et peu visible | **fort**. 27 000 mots de contenu thématique rejoignent le domaine qui vend vos cours |
| Facilité de gestion | deux outils, deux interfaces, deux identités | **un seul site**, une seule chaîne de publication, outils d'audit déjà en place |
| Potentiel long terme | limité. Le blog Wix ne bénéficie pas de vos pages de service | **élevé**. Base de la bibliothèque en 6 piliers |
| Risque de contenu dupliqué | nul | maîtrisé : canonical Wix vers WordPress, ou noindex de l'article Wix, **avant** publication sur WordPress |
| Maillage interne | impossible (liens sortants seulement) | complet : articles ↔ piliers ↔ services ↔ Calendly |
| Conservation du patrimoine | totale | totale. Wix reste en ligne, rien n'est supprimé, originaux archivés dans `wix/content/` |
| Cohérence de marque | moyenne (deux sites, deux styles) | **forte** : sabinekouli.com devient l'unique référence |
| Coût | gratuit | gratuit (pas de forfait Wix nécessaire grâce au canonical ou au noindex) |

## Recommandation : option B, progressive et sélective, avec la page passerelle de l'option A comme hub

1. **La page « Il était une voix – Explorer, comprendre et développer sa voix »** devient sur WordPress la **page pilier du blog** (`/il-etait-une-voix/`) : concept, approche, 6 piliers, articles incontournables, liens vers les services et Calendly.
   - Tant qu'un article n'est pas migré, la page renvoie vers sa version Wix.
   - Une fois migré, le lien pointe vers la version WordPress.
2. **La migration se fait par lots de 3 à 5 articles**, jamais en masse, chacun validé par vous :
   - texte original conservé dans son sens ; corrections proposées sous forme de **différences visibles** (avant/après), jamais imposées ;
   - ajout des H2/H3, des méta-descriptions, des ALT, des liens internes et de l'encadré « réserver un premier entretien » ;
   - **date d'origine conservée**, avec « mis à jour le … » quand le contenu change réellement ;
   - les fusions regroupent plusieurs articles Wix en un seul article WordPress plus complet ;
   - les articles de santé sont révisés avec des sources vérifiables, un avertissement « contenu pédagogique, ne remplace pas un avis médical », et sans posologie.
3. **Avant chaque mise en ligne sur WordPress**, dans l'ordre :
   1. réglage dans Wix (par vous) : canonical de l'article Wix vers l'URL WordPress, ou noindex si l'option canonical n'existe pas ;
   2. vérification dans le HTML Wix ;
   3. publication sur WordPress ;
   4. ajout dans l'article Wix d'un bandeau « Cet article a déménagé sur sabinekouli.com », facultatif.
   Les articles Wix ne sont **jamais supprimés**. Si un jour vous prenez un forfait Wix avec domaine, des redirections 301 pourront remplacer les canonical.
4. Les 2 articles « ne pas migrer pour l'instant » (remèdes naturels, growl) restent sur Wix ; nous déciderons plus tard.

## Structure d'URL WordPress proposée

- Hub : `/il-etait-une-voix/` (page).
- Catégories, sous une catégorie parente « Il était une voix » :
  - `/category/il-etait-une-voix/technique-vocale/`
  - `…/anatomie-physiologie-voix/`
  - `…/sciences-de-la-voix/`
  - `…/soins-de-la-voix/`
  - `…/voix-parlee/`
  - `…/voix-corps-expression/`
- Articles : `/<slug-court-sans-accents>/`, conforme aux permaliens actuels (exemple : `/voix-mixte/`, `/chanter-juste/`, `/echauffement-vocal/`).
- La catégorie existante `blog-il-etait-une-voix` (1 article) devient le parent ; elle est à renommer. Les étiquettes ne sont pas utilisées pour ces contenus.

## Prochaines validations demandées

- [ ] Option B acceptée ?
- [ ] Droits sur les 69 images Wix ?
- [ ] Le canonical personnalisé est-il proposé dans votre interface Wix (forfait gratuit) ?
- [ ] Premier lot pilote proposé : *Comment fonctionne notre appareil vocal*, *Voix mixte*, *Chanter juste*, et la fusion *Échauffement vocal* (5 articles regroupés en 1).
