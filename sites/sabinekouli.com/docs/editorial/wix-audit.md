# Audit du blog Wix « IL ÉTAIT UNE VOIX » (24/11/2026)

Source : https://matomswe7.wixsite.com/iletaitunevoix, exploré en entier par les sitemaps Wix (`blog-posts-sitemap.xml`, `blog-categories-sitemap.xml`) et la navigation, et pas seulement la page d'accueil.
Script : `scripts/wix_inventory.py`. Données : `wix/inventory.json`, `wix/inventory.csv` ; texte complet de chaque article dans `wix/content/<slug>.md`.

## Vue d'ensemble

| Élément | Constat |
|---|---|
| Articles | **52**, tous publiés entre le 1er et le 4 août 2023, jamais mis à jour |
| Volume | 27 615 mots, médiane de 464 mots par article (de 225 à 995) |
| Catégories Wix | Technique vocale (28), Pathologies de la voix (8), Éclats de voix : soins de la voix (6), Anatomie poétique de la voix (5), Science de la voix (3), aucune catégorie (2) |
| Pages | Accueil, Blog, Qui suis-je ? (environ 200 mots), Réservation en ligne (vide), Forum (vide). Pas de page Contact distincte |
| Adresse | sous-domaine gratuit `wixsite.com`, sans domaine personnalisé |
| Indexation | **accueil, blog, Qui suis-je, réservation et forum en `noindex`**. Les articles et les catégories n'ont pas de directive robots, donc ils sont indexables. Aucune trace dans les résultats de recherche testés. Visibilité Google probablement **très faible, voire nulle** (à confirmer si vous avez Search Console pour Wix) |
| Méta-descriptions | aucune. Seule l'`og:description` est générée automatiquement |
| Structure | **aucun H2 ni H3** dans les articles. Ce sont des listes à puces en paragraphes |
| Images | 69 images, **0 texte ALT** |
| Liens | 123 liens internes (navigation et catégories), **0 lien externe**, aucune source citée |
| Schema | BlogPosting (auteur Sabine Kouli), généré par Wix |
| Commentaires | aucun commentaire visible |

## Qualité éditoriale : points d'attention

1. **Style homogène et générique.** Les articles suivent un même modèle (introduction, liste de bénéfices, conclusion) et ont été publiés en 4 jours. Ils ne contiennent presque jamais d'expérience personnelle, d'anecdote de cours ni de point de vue de cheffe de chœur. Exceptions notables : *Je suis femme ténor et alors ?* et *La voix à cœur ouvert*, qui portent votre voix propre.
2. **Aucune source** dans les articles scientifiques : « des études ont montré », « les chercheurs »… Pour Google comme pour vos lecteurs, ces textes ne démontrent pas encore l'expertise qu'ils évoquent.
3. **Contenus de santé à risque.**
   - *Comment retrouver sa voix rapidement avec des remèdes naturels* donne des **posologies d'huiles essentielles par voie orale**.
   - Plusieurs articles parlent de « soigner » et de « traitement ».
   - Les articles sur les dysphonies décrivent des examens et des traitements médicaux sans source et sans renvoi clair vers un ORL ou un phoniatre.
   Ces contenus ne doivent pas être republiés en l'état (risque pour les lecteurs, et sujets que Google évalue avec une exigence particulière).
4. **Doublons et chevauchements :**
   - *Comment garder sa voix en bonne santé ?* existe **deux fois** (`…-bonne-santé` et `…-bonne-santé-1`), avec un texte quasi identique.
   - 5 articles sur l'échauffement, 3 sur la respiration abdominale, 2 sur les registres, 2 sur le vibrato, 2 sur la routine vocale, 3 sur les troubles de la voix : chaque groupe vise la **même recherche**. Il faut fusionner.
5. **Rien sur la voix parlée** (en dehors de la projection) : c'est un manque, alors que vous voulez développer le coaching voix et prise de parole.

## Classement par pilier

| Pilier proposé | Articles Wix | Contenus les plus utiles pour votre positionnement |
|---|---|---|
| 1. Technique vocale et apprentissage | 24 | voix mixte, voix de tête, voix de poitrine, justesse (« quand on chante très faux »), échauffement (fusion), respiration (fusion), vocalises, résonateurs, « Comment les cours de technique vocale enrichissent le parcours des amateurs » |
| 2. Anatomie et physiologie | 6 | Comment fonctionne notre appareil vocal, Les différents types de voix, Le timbre, Les muscles de la voix |
| 3. Sciences de la voix | 3 | Acoustique et physiologie, Analyse spectrale (à sourcer) |
| 4. Soins et préservation | 15 | Garder sa voix en bonne santé (fusion), Surmenage vocal, Prévention. Les articles « pathologies » sont à réviser |
| 5. Voix parlée et professionnelle | 1 | Projection de la voix |
| 6. Voix, corps et expression | 3 | Je suis femme ténor et alors ?, Chanter avec confiance et émotion, Mise en route corporelle |

Détail article par article (action, priorité, slug proposé) : `wix-wordpress-mapping.csv`.

## Contenus WordPress existants sur la voix

Sur les 137 articles WordPress, 25 parlent de chant ou de gospel. Ce sont **tous des actualités** (stages datés, saisons, concerts, festival). **Aucun article pédagogique** : les contenus Wix comblent un vide, sans concurrence directe. Seul risque : les pages de service (coaching, stage) face aux articles sur l'intérêt des cours, à gérer par le maillage.
