# Positionnement gospel : chanteuse, cheffe de chœur, fondatrice du festival Absolute Gospel

Demande de Sabine du 24/11/2026 : le SEO doit renforcer **deux identités complémentaires**, sans qu'elles se concurrencent :
1. **Artiste gospel** : chanteuse gospel, cheffe de chœur gospel, fondatrice du festival Absolute Gospel à Lyon.
2. **Pédagogue de la voix** : coach vocal, cours de chant, technique vocale, « Il était une voix ».

Le gospel est aussi un **atout de différenciation** pour le coaching : peu de coachs vocaux lyonnais ont ce parcours de scène et de direction de chœur.

> Nom du festival : le site emploie « **Absolute Gospel** ». Votre message dit « Absolue gospel » : je retiens « Absolute Gospel », **à confirmer**.

## 1. Une intention de recherche = une page

| Recherche visée | Page cible (existante) | État au 24/11 | Action |
|---|---|---|---|
| Sabine Kouli (marque), chanteuse gospel Lyon, cheffe de chœur gospel Lyon | **Bio** `/sabine-kouli-chanteuse-gospel/` (97) | titre « Sabine Kouli - Sabine Kouli », 4 images sans ALT, 1 lien en 404 | titre, méta, ALT, lien. Parcours enrichi par vous : 25 ans, chœurs dirigés, scènes (Opéra de Lyon, etc.) |
| chorale gospel Lyon, chœur gospel Lyon, rejoindre une chorale gospel | **La Jaama** `/sabine-kouli-concerts-groupes/chorale-gospel-la-jaama/` (121) | 459 mots, **13 images sans ALT**, sans méta | page de recrutement : répétitions, niveau, comment rejoindre (infos réelles à fournir), CTA |
| chanteuse gospel mariage Lyon, gospel mariage, chanteuse pour cérémonie | **Événements privés** `.../je-chante-pour-votre-evenement/` (294) | **94 mots**, 9 images sans ALT, titre « Evènements privés » | forte valeur commerciale, page à enrichir en priorité |
| animation gospel entreprise, team building chant gospel | **Team building** (296) | 328 mots | titre, méta, ALT |
| stage gospel Lyon, stage negro-spirituals | **Stage Gospel et Negro-spirituals** (744) | 141 mots | enrichir, avec dates **réelles** uniquement |
| concert gospel Lyon, groupe gospel Lyon | **Spectacles** (412) : hub des formations | **46 mots** | texte d'introduction, liens vers chaque formation |
| Lyon Gospel Mass Choir, Symphonic Gospel, Gospel Jam | pages formations (536, 259, 257) | 280-410 mots | titres, méta, ALT ; Schema `MusicGroup` |
| festival gospel Lyon, festival Absolute Gospel | **absolutegospel.fr** (site officiel) | indexé, **sans mention de Sabine ni lien** | ne pas concurrencer le site officiel. Sur sabinekouli.com, la page festival (267) raconte **votre rôle de fondatrice** et renvoie vers absolutegospel.fr |

**Accueil** : il porte l'entité « Sabine Kouli » et ses deux identités ; il ne cible pas une seule requête de service.
Titre d'accueil **révisé** (il remplace la proposition du 13/11, à valider) :
- Titre SEO (52 car.) : *Sabine Kouli – Chanteuse gospel et coach vocal à Lyon*
- H1 (inchangé) : *Sabine Kouli – Chanteuse gospel et coach vocal à Lyon*
- Méta (149 car.) : *Chanteuse et cheffe de chœur gospel depuis 25 ans, fondatrice du festival Absolute Gospel, Sabine Kouli vous accompagne en coaching vocal à Lyon ou en visio.*

La recherche « coach vocal Lyon » reste confiée à la page coaching.

## 2. Données structurées : relier les entités

Dans le graphe Yoast (filtre `wpseo_schema_graph`, sans second bloc JSON-LD) :
- `Person` Sabine Kouli :
  - `jobTitle` : « Chanteuse gospel, cheffe de chœur et coach vocal » ;
  - `sameAs` : Facebook artiste, Instagram, LinkedIn ;
  - `founder` du festival → `@id` du festival.
- `Festival` / `Organization` « Absolute Gospel » : `url` = absolutegospel.fr, `founder` → Person. Une fiche d'entité, pas d'événements.
- `MusicGroup` pour La Jaama, Lyon Gospel Mass Choir, Symphonic Gospel… : `genre` Gospel, avec la direction artistique (`member` ou `founder` → Person, selon votre rôle réel).
- `MusicEvent` **uniquement** pour des concerts réels et datés.

## 3. Le festival : un levier d'autorité

1. **Sur absolutegospel.fr** (site séparé, à configurer à part si vous le souhaitez, avec ses propres identifiants) :
   - ajouter une mention « Festival fondé par Sabine Kouli », avec un lien vers sabinekouli.com ;
   - ajouter dans le Schema du festival `founder` → Sabine Kouli, avec `sameAs` sabinekouli.com.
2. **Sur sabinekouli.com** : la page festival renvoie vers absolutegospel.fr (programme, billetterie).
3. **Presse et partenaires** : le festival génère des articles (presse locale, agendas, ville de Lyon). Demander que ces articles citent « Sabine Kouli, fondatrice » avec un lien vers sabinekouli.com : c'est le meilleur levier de notoriété pour le site.

## 4. Septième pilier éditorial : « Gospel, chœur et spirituals »

S'ajoute aux 6 piliers « voix ». Il relie l'expertise artistique à la pédagogie.

| Sujet d'article (exemples) | Intention | Vers le service |
|---|---|---|
| Gospel et negro-spirituals : quelles différences ? (histoire, sources sérieuses) | informationnelle | stage Negro-spirituals |
| Chanter le gospel : souffle, placement, mélismes, appel-réponse | technique | coaching, stage |
| Diriger un chœur gospel : ce que 25 ans de direction m'ont appris | expertise personnelle | La Jaama, team building |
| Rejoindre une chorale gospel à Lyon : à quoi s'attendre ? | locale, transactionnelle | La Jaama |
| Gospel pour un mariage : répertoire et organisation | commerciale | Événements privés |
| Histoire du gospel à Lyon et naissance du festival Absolute Gospel | notoriété | page festival, absolutegospel.fr |

Les 25 articles d'actualité WordPress sur le gospel (concerts, saisons, festival) seront reliés à ce pilier. Ce sont des preuves d'activité réelle.

## 5. Informations à fournir (rien ne sera inventé)

- Confirmation du nom du festival (Absolute Gospel) et de l'année de création.
- Votre rôle exact dans chaque formation (fondatrice, directrice, soliste).
- La Jaama : jour et lieu de répétition, niveau requis, modalités pour rejoindre (si le recrutement est ouvert).
- Références de scène vérifiables à mettre en avant (Opéra de Lyon, festivals, partenaires).
- Accès à absolutegospel.fr : même procédure de connexion, en tant que site séparé.
