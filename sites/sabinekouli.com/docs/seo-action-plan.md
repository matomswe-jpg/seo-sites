# sabinekouli.com : plan d'action SEO hiérarchisé

Version 1 du 24/11/2026, établie à partir de l'audit en lecture seule (`seo-baseline.md`).
Légende du niveau :
- 🔍 lecture seule
- 📝 préparé localement
- ✋ validation requise avant exécution
- 🔒 impossible sans accès supplémentaire

Aucun résultat de classement n'est promis. Les effets se mesureront dans Search Console et dans les statistiques de la fiche Google.

## Phase 0 : prérequis (à faire par vous)

| # | Action | Niveau | Qui |
|---|---|---|---|
| 0.1 | Vérifier, dans l'espace client OVH, la date de la dernière sauvegarde (fichiers et base), puis faire une sauvegarde manuelle | 🔒 | vous |
| 0.2 | Réactiver les Application Passwords dans Wordfence, créer `seo-technique` (Éditeur) et son mot de passe d'application (voir `docs/wordpress-connection.md`) | 🔒 | vous |
| 0.3 | Donner un accès à Google Search Console (ou m'envoyer les exports *Performances* et *Pages* sur 16 mois) | 🔒 | vous |
| 0.4 | Valider les éléments `[À VALIDER]` de `site.md` : nom exact de la fiche Google, accueil réel à la Maison Ferber, « 25 ans », page Facebook officielle, lien de la fiche Google | ✋ | vous |
| 0.5 | Indiquer votre offre OVH (Perso, Pro, Performance), pour savoir si SSH et WP-CLI sont disponibles en dernier recours | 🔒 | vous |

## Phase 1 : corrections rapides à fort impact (semaine 1)

| Prio | URL | Problème | Correction proposée | Niveau |
|---|---|---|---|---|
| P1 | `/` (ID 12) | Titre « Home - Sabine Kouli », sans méta | Titre : *Coach vocal à Lyon & Caluire – Cours de chant \| Sabine Kouli* (58 car.). Méta : texte ci-dessous | 📝 puis ✋ |
| P1 | `/pedagogies-vocales/cours-et-coaching-vocal/` (553) | Sans méta, titre générique | Titre : *Coaching vocal à Lyon-Caluire et en visio – Sabine Kouli* (55). Méta : texte du plan | 📝 puis ✋ |
| P1 | `/sabine-kouli-chanteuse-gospel/` (97) | Titre en doublon | *Sabine Kouli – Chanteuse gospel, cheffe de chœur & coach vocal* (61). Méta : texte du plan (« originaire du Togo » à confirmer) | 📝 puis ✋ |
| P1 | `/infos-pratiques/contact/` (792) | Sans méta, sans NAP | Titre : *Contact – Sabine Kouli, coach vocal à Caluire (Lyon)* (52) | 📝 puis ✋ |
| P1 | `/pedagogies-vocales/` (269) | Sans méta | *Cours, stages et ateliers de chant à Lyon – Sabine Kouli* (55) | 📝 puis ✋ |
| P1 | `/stage-de-technique-vocale/` (3669) | Sans méta, orpheline | *Stage de technique vocale à Lyon – Sabine Kouli* (47). Ajouter un lien depuis la page Pédagogie vocale et la page coaching. Méta sans le mot « tarifs » tant qu'aucun tarif n'est affiché | 📝 puis ✋ |
| P1 | bio (97) | Lien interne en 404 vers `/pedagogies-vocales/gospel-negro-spirituals/` | Remplacer par `/stage-thematique-negro-spirituals/` (destination probable, à confirmer) | ✋ |
| P1 | `/couleurs-du-pelourinho-salvador-da-bahia/` | Lien « bali & thailande » mal formé (404) | Corriger vers l'article visé ou retirer le lien | ✋ |
| P1 | `/` | Pas de H1 | Transformer le premier titre « Sabine Kouli » (H3) en H1 : *Sabine Kouli – Chanteuse gospel et coach vocal à Lyon*. L'accueil est généré par le **thème** : à faire dans *Apparence > Personnaliser*, ou dans un modèle du thème | ✋ (touche au thème) |

Méta-description de l'accueil, sans chiffre non validé :
> Chanteuse gospel et coach vocal, Sabine Kouli vous accompagne à Caluire (Lyon) ou en visio : technique vocale, confiance, scène. 1er RDV offert. (143 car.)

**Méthode d'écriture des titres et méta :** capacité `yoast-seo/update-post-seo-data` si elle est exposée. Sinon WP-CLI, sinon saisie guidée. Essai d'abord sur **une seule** page (la page coaching), contrôle du HTML publié, puis le reste du lot.

## Phase 2 : nettoyage (semaine 1-2)

| Prio | Élément | Constat vérifié | Proposition | Niveau |
|---|---|---|---|---|
| P1 | `/sdfqsdf/` (900) | page de test, 1 mot, 0 lien entrant | Mettre à la corbeille, sans vider la corbeille pendant 30 jours (restauration possible). Il restera un 404 propre, ou une 410 si vous le souhaitez | ✋ |
| P1 | `/home-2/` (706) | vide, 0 lien entrant | Même traitement | ✋ |
| P1 | `/about/` (ID 1) | texte par défaut de WordPress, 0 lien entrant | Redirection 301 vers `/sabine-kouli-chanteuse-gospel/` (pertinente : c'est la page « à propos » réelle), puis corbeille. **Aucun outil de redirection n'est installé** : extension « Redirection » (gratuite) ou règle `.htaccess` | ✋ |
| P2 | 76 archives d'étiquettes | 57 n'ont qu'un article, 11 n'en ont aucun, aucune n'a de contenu propre | `noindex` global des étiquettes via *Yoast > Réglages > Taxonomies > Étiquettes*, après vérification dans Search Console qu'aucune ne reçoit de clics. Pas de blocage dans robots.txt | 🔒 GSC puis ✋ |
| P2 | Archives d'auteur (2) | site à auteur unique, slugs qui ressemblent à des identifiants | *Yoast > Réglages > Avancé > Archives d'auteur* : désactiver. Cela retire aussi l'author-sitemap. Changer le « nom à afficher » des comptes | ✋ |
| P3 | Catégorie « uncategorized » (17 articles) | catégorie par défaut, nom anglais | Renommer (par exemple « Actualités ») ou réaffecter les articles | ✋ |
| P3 | `/infos-pratiques/` « Pratik » | titre peu explicite | Titre SEO : *Infos pratiques – Sabine Kouli* | 📝 |
| P3 | `/boutique-afromad/`, `/documentaires/` (contenu vide) | pages sans contenu | Vérifier leur utilité : contenu, noindex ou redirection | ✋ |

## Phase 3 : NAP et local (semaine 2)

1. **Pied de page :** bloc NAP identique à la fiche Google, une fois le nom exact confirmé.
   ```
   Sabine Kouli – Coach vocal      ← ou « Sabine Kouli », selon le nom réel de la fiche
   Maison Ferber, 14 rue du Capitaine Ferber, 69300 Caluire-et-Cuire
   06 61 44 42 87 (lien tel:+33661444287) · Itinéraire
   ```
   Le pied de page est un widget du thème : il faut votre accord (✋, touche au design).
2. **Page Contact :** même bloc, plus le lien Calendly. Brouillon dans `drafts/` (📝).
3. **Page coaching :** section « Où ont lieu les cours » avec les deux lieux et la mention « le lieu exact est communiqué lors de la réservation ».
4. **Condition préalable :** n'afficher la Maison Ferber comme adresse professionnelle (site, Schema, fiche Google) que si vous y recevez effectivement vos élèves et pouvez le justifier (0.4). Sinon : fiche Google en zone desservie, sans adresse, et site en mode « lieux de cours ».

## Phase 4 : architecture des pages et contenus

### Décision recommandée sur `/coach-vocal-lyon/`

La page existante `/pedagogies-vocales/cours-et-coaching-vocal/` cible **exactement la même intention** (« coach vocal Lyon », « cours de chant Lyon/Caluire », coaching individuel en présentiel). Créer `/coach-vocal-lyon/` en plus produirait deux pages concurrentes, dont une sans historique ni liens.

**Recommandation : ne pas créer `/coach-vocal-lyon/` pour l'instant.** Faire de la page coaching existante **la** page commerciale locale :
- garder son URL (ancienneté, liens du menu, futur lien de la fiche Google) ;
- l'enrichir jusqu'à 900-1 200 mots : présentation, publics (débutants, confirmés, auditions et concours, prise de parole, professionnels de la voix), méthode (souffle, posture, résonance, justesse, interprétation), présentiel (2 lieux) et visio, Calendly en haut et en bas, FAQ de 5 questions, puis tarifs et témoignages **une fois fournis** ;
- réévaluer dans 3 mois, selon les requêtes Search Console. Si « coach vocal Lyon » ne remonte pas, on étudiera un changement de slug avec redirection 301 plutôt qu'une page en plus.

### Pages complémentaires (intentions distinctes, sans cannibalisation)

| Page | Intention | Distinction avec la page coaching | Niveau |
|---|---|---|---|
| `/cours-de-chant-en-ligne/` | chercheurs nationaux et francophones, « cours de chant en ligne », « coaching vocal à distance » | aucune notion locale. Déroulé d'une séance en visio, matériel, fuseaux horaires | 📝 brouillon, puis ✋ publication |
| `/coaching-voix-prise-de-parole/` | voix **parlée** : enseignants, formateurs, avocats, conférenciers, fatigue vocale | pas de chant, public professionnel. Ne pas promettre d'effet thérapeutique (renvoyer vers un ORL ou un orthophoniste en cas de pathologie) | 📝 brouillon, puis ✋ publication |

Maillage : coaching ↔ en ligne ↔ prise de parole, chacune → Contact et Calendly. Pédagogie vocale → les trois. Stage → coaching.

**FAQ :** bloc FAQ Yoast. Depuis 2023, Google n'affiche plus les résultats enrichis FAQ pour ce type de site. L'intérêt est donc éditorial (répondre aux questions et aux requêtes conversationnelles), pas un affichage enrichi.

## Phase 5 : données structurées

Constat : Yoast déclare le site comme **Organization** (« Sabine Kouli », logo), sans adresse, sans téléphone et sans `sameAs`.

Recommandation, dans l'ordre de préférence :
1. **Natif Yoast, sans code** : *Yoast > Réglages > Représentation du site* → « Personne », avec le compte de Sabine. Renseigner sa photo et ses profils sociaux dans son profil utilisateur (`sameAs`). Le graphe devient cohérent (`#/schema/person/...`) sans doublon. ✋ (réglage global)
2. **Activité locale :** le type `ProfessionalService` du plan **n'est pas recommandé**. Schema.org l'indique comme déprécié pour les entreprises locales, à cause de la confusion avec `Service`. Types possibles : `LocalBusiness` générique, avec `founder` → Person, `address` (Maison Ferber), `telephone`, `areaServed`, `hasMap` (lien de la fiche Google), `makesOffer` (services réellement proposés). Google lit surtout la fiche Business Profile pour le pack local. Ce balisage sert la **cohérence**, sans garantie d'affichage.
   - Mise en œuvre sans doublon : ajouter le nœud **au graphe Yoast** par le filtre `wpseo_schema_graph` (petit plugin « must-use », ou extension Yoast Local SEO, payante). **Pas** de bloc JSON-LD collé à part avec WPCode, qui créerait un second graphe.
   - Le code est préparé dans `drafts/schema-localbusiness.php` (📝, à venir), puis installé après votre accord et la confirmation de l'adresse (✋, 🔒 SSH/FTP ou accès admin).
3. Validation : Rich Results Test et validator.schema.org, en contrôlant que les identifiants `@id` restent stables.

## Phase 6 : images

- Bio (97) : 4 images sur 5 sans ALT. Pédagogie : 1. Articles : environ 60 articles concernés (voir `issues.md`).
- Méthode : ALT modifié dans la médiathèque via l'API REST (`alt_text`), sans toucher aux fichiers. Textes ALT descriptifs, rédigés après avoir **vu** l'image, sans accumulation de mots-clés. Liste préparée pour validation, page par page (📝 puis ✋).
- Le poids et les formats seront analysés par une seconde passe (les images sont en lazy-load via LiteSpeed). La conversion WebP de LiteSpeed sera vérifiée ensuite.

## Phase 7 : Google Business Profile (mission séparée)

Textes du plan repris, avec ces correctifs :
- Description : retirer « plus de 25 ans » tant que le chiffre n'est pas validé.
- Lien du site : page coaching, avec paramètres UTM. OK.
- Nom : celui de la fiche réelle, sans mot-clé ajouté.
- Pas d'accès, donc aucune modification de ma part : textes à valider puis à saisir par vous.

## Phase 8 : suivi

- Search Console : groupe de requêtes prioritaires (coach vocal lyon, cours de chant caluire, coaching vocal visio, cours de chant lyon, technique vocale, cours de chant saint-clair, coaching vocal individuel, coaching voix prise de parole). Relevé mensuel des impressions, clics et positions moyennes.
- Avant/après sur 28 jours pour chaque lot de modifications, consigné dans `seo-validation.md`.
- Fiche Google : appels, clics vers le site, itinéraires (relevé mensuel par vous).

## Ordre d'exécution proposé

1. Phase 0 (vous).
2. Connexion vérifiée, `check_connection.py`, export de l'état initial authentifié (`backups/`).
3. Essai : titre et méta de la page coaching seule, puis contrôle.
4. Lot titres et méta (5 autres pages).
5. Corrections des 404 et maillage de la page de stage.
6. Nettoyage : corbeille, redirection de `/about/`, étiquettes en noindex (après GSC), archives d'auteur.
7. Représentation Yoast en « Personne », puis NAP, puis nœud LocalBusiness.
8. Enrichissement de la page coaching, puis brouillons des deux nouvelles pages.
9. ALT des images par lots.

## Mise à jour du 24/11/2026 : positionnement gospel

Demande : renforcer aussi l'identité chanteuse gospel, cheffe de chœur gospel et fondatrice du festival Absolute Gospel. Détail dans `docs/editorial/gospel-positioning.md`.
- **Accueil** : titre révisé en *Sabine Kouli – Chanteuse gospel et coach vocal à Lyon*, avec une méta citant les 25 ans, le festival et le coaching. Il remplace la proposition de la phase 1 (à valider). La recherche « coach vocal Lyon » reste portée par la page coaching.
- Pages gospel ajoutées au lot titres, méta et ALT : bio (97), La Jaama (121), Événements privés (294), Team building (296), Stage Negro-spirituals (744), Spectacles (412), Festival (267), formations (536, 259, 257).
- Schema : `founder` → festival, `MusicGroup` pour les formations.
- absolutegospel.fr : lien et mention « fondé par Sabine Kouli » à ajouter (site séparé).
- 7e pilier éditorial : « Gospel, chœur et spirituals ».

## Mise à jour du 24/11/2026 : écosystème des 4 sites

- Titre d'accueil *Sabine Kouli – Chanteuse gospel et coach vocal à Lyon* : **approuvé** par Sabine le 24/11/2026. À exécuter dès que l'accès est en place (lecture de l'état initial, modification, puis contrôle du HTML publié).
- Liens vers lajaama.fr, absolutegospel.fr et baobabetcie.fr : voir `docs/ecosystem.md` §3 (pages 97, 121, 267, 301, pied de page).
- Schema : Person `@id` = `https://sabinekouli.com/#person` (identifiant partagé par les 4 sites).
- Fiche Google Sabine Kouli : **zone desservie validée le 24/11/2026**.

## Mise à jour du 2026-11-24 : zone desservie validée (remplace les phases 3 et 5 sur ces points)

**Phase 3 (NAP) révisée**
- Pied de page : `Sabine Kouli – coach vocal · 06 61 44 42 87 (tel:+33661444287) · Cours à Caluire-et-Cuire, Lyon et en visio`. Pas d'adresse postale dans le pied de page.
- Page coaching et page Contact : section « Où ont lieu les cours », avec les deux lieux (Maison Ferber, 14 rue du Capitaine Ferber ; Maison de quartier de Saint-Clair, 82B Grande Rue de Saint-Clair, 69300 Caluire-et-Cuire) et la mention « le lieu exact est communiqué lors de la réservation ».
- Le nom affiché sur le site doit rester identique au nom de la fiche Google (toujours à confirmer).

**Phase 5 (Schema) révisée**
- Pas de nœud `LocalBusiness` avec adresse Maison Ferber, qui aurait recréé la confusion avec La Jaama.
- Person `#person` : `jobTitle`, `telephone`, `areaServed` (villes ci-dessus), `sameAs` (Instagram coach vocal, Facebook artiste, LinkedIn, fiche Google via son URL `kgmid`), `founder` → festival et Baobab selon `docs/ecosystem.md`.
- Page coaching : nœud `Service` (« Coaching vocal individuel », `provider` → #person, `areaServed`, `availableChannel` présentiel et visio) ajouté au graphe Yoast.

**Fiche Google : étapes pour Sabine (5 minutes)**
1. business.google.com (ou recherche Google « Sabine Kouli », puis « Modifier le profil »).
2. **Infos > Emplacement et zones > Adresse de l'établissement** : **retirez l'adresse** (ou choisissez de ne pas l'afficher), puis enregistrez.
3. **Zone desservie** : ajoutez Caluire-et-Cuire, Lyon, Rillieux-la-Pape, Villeurbanne.
4. Vérifiez que le nom est exactement celui de votre activité, sans mot-clé ajouté.
5. Google peut demander une nouvelle validation après le changement : c'est normal.
