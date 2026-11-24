# Écosystème Sabine Kouli : 4 sites, 4 fiches Google, une seule cohérence

Mis à jour le 24/11/2026. Sources : les 5 plans fournis (13/11/2026, archivés dans `sites/<site>/docs/sources/`), audits en lecture seule du 24/11/2026, réponses de Sabine.

## 1. Rôle de chaque site (une recherche = un site)

| Site | Entité | Rôle | Recherches visées | Fiche Google |
|---|---|---|---|---|
| **sabinekouli.com** | Sabine Kouli (Person) | l'artiste et la pédagogue : coaching, cours, stages, prestations, « Il était une voix » | coach vocal Lyon, cours de chant Caluire/Lyon/visio, chanteuse gospel (mariage), cheffe de chœur gospel | [Sabine Kouli](https://g.co/kgs/zUP8xPZ) (kgmid `/g/11vcm_x5td`) |
| **lajaama.fr** | La Jaama (MusicGroup), depuis 1999 | la chorale | chorale gospel (Lyon), cours gospel Lyon, rejoindre une chorale | [La Jaama](https://g.co/kgs/v9H2JRe) (kgmid `/g/11vdg624y7`) |
| **absolutegospel.fr** | Festival Absolute Gospel (EventSeries), depuis 2004 | le festival | festival gospel Lyon, concert gospel Lyon | [Festival](https://g.co/kgs/ykByczA) (kgmid `/g/11y5cnp_c6`) |
| **baobabetcie.fr** | Association Baobab & Compagnie (Organization), depuis 2002 | la « maison mère » : relie et oriente vers les 3 autres sites | association gospel Lyon, Baobab et Compagnie | nouvelle fiche (lien à fournir) |

Règles :
- Chaque site a **ses propres identifiants**, son dossier `sites/<domaine>/` et son audit. Rien n'est mutualisé.
- sabinekouli.com **ne concurrence pas** lajaama.fr sur « chorale gospel », ni absolutegospel.fr sur « festival gospel ». Ses pages La Jaama et Festival présentent **votre rôle** et renvoient vers le site officiel.

## 2. Liens entre les sites : état mesuré le 24/11/2026

Scan des pages publiques (sitemaps) :

| Depuis ↓ / vers → | sabinekouli.com | lajaama.fr | absolutegospel.fr | baobabetcie.fr |
|---|---|---|---|---|
| **sabinekouli.com** | — | ❌ 0 page | ❌ 0 page | ❌ 0 page |
| **lajaama.fr** | ⚠️ 1 page (agenda) | — | ✅ pied de page | ✅ pied de page |
| **absolutegospel.fr** | ❌ 0 | ❌ 0 | — | ❌ 0 |
| **baobabetcie.fr** | ✅ pied de page | ✅ pied de page | ✅ pied de page | — |

sabinekouli.com et absolutegospel.fr, les deux sites les plus anciens, **ne renvoient vers aucun autre site**.
Note : le plan sabinekouli du 13/11 indiquait « sabinekouli.com → absolutegospel.fr (déjà présent) ». Ces liens existent seulement dans d'anciens articles, sans lien dans le texte des pages principales.

## 3. Liens à ajouter (validation requise sur chaque site)

1. **Bloc « Nos sites »** identique dans le pied de page des 4 sites, en `https://` sans `www` :
   *Baobab & Compagnie – l'association · Sabine Kouli – chanteuse et coach vocal · La Jaama – chorale gospel · Festival Absolute Gospel*
2. **Liens dans le texte** (ce sont eux qui comptent le plus) :

| Site | Page | Lien vers | Texte du lien |
|---|---|---|---|
| sabinekouli.com | La Jaama (121) + article `/chorale-de-gospel-a-lyon-la-jaama/` | lajaama.fr (page « Rejoindre ») | « Rejoindre la chorale gospel La Jaama » |
| sabinekouli.com | Festival Absolute Gospel (267) | absolutegospel.fr | « Programmation du Festival Absolute Gospel » |
| sabinekouli.com | Bio (97) | baobabetcie.fr, lajaama.fr, absolutegospel.fr | « l'association Baobab & Compagnie », « La Jaama », « Festival Absolute Gospel » |
| sabinekouli.com | Sites associés (301) | les 3 sites | noms des sites |
| absolutegospel.fr | À propos | sabinekouli.com, baobabetcie.fr | « fondé par Sabine Kouli », « association Baobab & Compagnie » |
| absolutegospel.fr | articles La Jaama | lajaama.fr | « la chorale gospel La Jaama » |
| absolutegospel.fr | Infos pratiques (organisateur) | baobabetcie.fr | « Association Baobab & Compagnie » |
| lajaama.fr | Accueil, page Rejoindre | sabinekouli.com, absolutegospel.fr | « Sabine Kouli, cheffe de chœur », « Festival Absolute Gospel » |
| baobabetcie.fr | Nos activités | tous (page fournie, 30 liens) | — |

3. **Fiches Google** : chaque description mentionne les autres entités (« portée par l'association Baobab & Compagnie »). Chaque fiche ne parle que de **sa** propre activité.
4. **Réseaux sociaux** : en bio, le site correspondant à chaque compte.

## 4. Données structurées : un seul jeu d'identifiants partagé

Les 4 plans proposent chacun un bloc JSON-LD. **Ils se contredisent sur les identifiants.** Voici les identifiants de référence, à utiliser sur tous les sites :

| Entité | `@id` de référence | Type | Déclarée sur |
|---|---|---|---|
| Sabine Kouli | `https://sabinekouli.com/#person` | Person | sabinekouli.com (représentation Yoast « Personne », `@id` fixé par filtre) |
| Baobab & Compagnie | `https://baobabetcie.fr/#association` | Organization (`legalName`, `foundingDate` 2002-08-29, SIRET) | baobabetcie.fr |
| La Jaama | `https://lajaama.fr/#chorale` | MusicGroup (`foundingDate` 1999, `founder` → #person) | lajaama.fr |
| Festival Absolute Gospel | `https://absolutegospel.fr/#festival` | EventSeries (`startDate` 2004, `organizer` → baobabetcie.fr/#association) | absolutegospel.fr |

Sur les autres sites, on **référence** ces `@id` sans redéclarer l'entité complète.

**Corrections apportées aux plans :**
- Plan du festival : le nœud `https://absolutegospel.fr/#association`, de type **PerformingArtsTheater** (nommé « Festival Absolute Gospel », `legalName` Baobab), **n'est pas retenu**. Ce type désigne une salle de spectacle, et il créerait une seconde association. L'organisateur devient `{"@id": "https://baobabetcie.fr/#association"}`.
- Plan La Jaama : `founder` est une Person sans `@id`. Il devient `{"@id": "https://sabinekouli.com/#person"}`.
- Plan sabinekouli : le type `ProfessionalService` est abandonné (voir `sites/sabinekouli.com/docs/seo-action-plan.md`).
- Sites avec Yoast (sabinekouli, absolutegospel) : les nœuds sont ajoutés **au graphe Yoast** (filtre `wpseo_schema_graph`), pas dans un second bloc WPCode, pour éviter deux graphes concurrents.
- lajaama.fr et baobabetcie.fr n'ont pas encore Yoast. Si Yoast y est installé (recommandé par les plans), on applique la même règle.

## 5. Fiches Google : éviter les confusions

| Fiche | Nom exact (sans mot-clé) | Catégorie principale | Adresse | Téléphone |
|---|---|---|---|---|
| Sabine Kouli | Sabine Kouli | Professeur de chant | ⚠️ **décision** (voir ci-dessous) | 06 61 44 42 87 |
| La Jaama | La Jaama | Chœur | Maison Ferber, 14 rue du Capitaine Ferber, Caluire | 06 61 44 42 87 |
| Festival | Festival Absolute Gospel | Festival / Organisateur d'événements | 104 route de Strasbourg si accueil du public, sinon zone desservie | 07 83 99 99 75 (Infoline) |
| Baobab | Association Baobab & Compagnie | Association culturelle | **zone desservie** : le guide indique « pas d'accueil du public » au 104 route de Strasbourg | 06 61 44 42 87 |

⚠️ **Décision à prendre : l'adresse de la fiche Sabine Kouli.**
- Le plan sabinekouli (13/11) propose la Maison Ferber, et vous avez confirmé y recevoir vos élèves.
- Le plan Baobab propose une « zone desservie ».
- Or **La Jaama est déjà à la Maison Ferber, avec le même téléphone**. Deux fiches à la même adresse, avec le même numéro et des activités proches (chant), présentent un **risque réel de fusion ou de filtrage par Google**.
- Recommandation : fiche Sabine Kouli en **zone desservie**, adresse masquée. Les deux lieux de cours restent sur sabinekouli.com et dans son Schema (lieux où se déroulent les cours), ce qui est correct.

À vérifier : le plan La Jaama mentionne une **cinquième fiche**, « Sabine Kouli – Chanteuse Gospel Lyon ». Si c'est un doublon de votre fiche, il faut demander la fusion à Google, et ne pas créer d'autre fiche.
Les noms actuels de fiches qui contiennent des mots-clés (« CHORALE GOSPEL LYON LA JAAMA », « FESTIVAL ABSOLUTE GOSPEL LYON ») sont à corriger en priorité.

## 6. Faits de référence (validés ou issus de vos documents)

| Fait | Valeur | Statut |
|---|---|---|
| La Jaama : création | 1999 | plan La Jaama |
| La Jaama : répétitions | mardi 19 h – 21 h, Maison Ferber, 14 rue du Capitaine Ferber, 69300 Caluire-et-Cuire | **confirmé par Sabine le 24/11** |
| La Jaama : niveau | débutants en gospel bienvenus, **il faut savoir chanter juste** | **confirmé par Sabine le 24/11**. ⚠️ Le plan disait « débutants comme confirmés » : à reformuler |
| La Jaama : tarif | 330 €/an, payable en 3 ou 5 fois, essai offert | plan La Jaama, à reconfirmer avant publication |
| Baobab : création | 29/08/2002, SIRET 444 056 758 00014 | plan Baobab |
| Festival : création | 2004 ; 22e édition les 5-6 juin 2026 | plans ; « 22 éditions en 23 ans » à confirmer (une année sans édition ?) |
| Festival 2026 | **vendredi** 5 et **samedi** 6 juin 2026 | vérifié au calendrier ; le site affiche « samedi 5 juin » et « 6 juin 2025 » (erreurs) |
| Festival 2027 (23e édition) | **samedi 5 et dimanche 6 juin 2027**, Salle Molière, 20 quai de Bondy, 69005 Lyon | **confirmé par Sabine le 24/11/2026** ; jours de semaine vérifiés |
| Salle Molière | 20 quai de Bondy, 69005 Lyon | **confirmé par Sabine le 24/11/2026**, conforme à la [Ville de Lyon](https://lyon.fr/lieu/salles-municipales-louer/salle-moliere-salle-de-spectacle-municipale) (le plan festival indiquait « 18 ») |
| Infoline festival | 07 83 99 99 75 | plan festival |
| Instagram | @sabinekouli_coachvocal (coaching), @lafromad (projets et voyages), @jaama_gospel, @absolutegospelfestival | guide Baobab : le lien « insta de Sabine Kouli » sur baobabetcie.fr doit pointer vers @sabinekouli_coachvocal |

## 7. Constats des plans vérifiés le 24/11/2026

| Constat | Vérifié |
|---|---|
| lajaama.fr et baobabetcie.fr répondent en `http://` sans rediriger vers https | ✅ (HTTP 200 en http) |
| baobabetcie.fr : pages de démonstration en ligne (`/sample-page/`, `/hello-world/`) | ✅ (HTTP 200) |
| lajaama.fr : articles vides « Actualité la Jaama 1… » | ✅ |
| lajaama.fr : ni « mardi » ni « Ferber » sur l'accueil | ✅ |
| absolutegospel.fr : page Contact vide, sans formulaire ni Infoline | ✅ |
| absolutegospel.fr : dates erronées sur l'accueil (« SAMEDI 6 JUIN 2025 », « SAMEDI 5 JUIN 2026 »), rien sur 2027 | ✅ |
| Les 4 sites : Wordfence actif, Application Passwords non exposées | ✅ |

Détails par site : `sites/<site>/audit/2026-11-24/issues.md`.
