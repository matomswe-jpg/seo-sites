# Nouveau groupe : informations à réunir avant rédaction (phase 5)

État : **aucune information disponible**. Aucun document ne m'a été transmis, et rien sur sabinekouli.com ne mentionne un groupe récent distinct des formations connues :
- La Jaama (chorale gospel) ;
- Lyon Gospel Mass Choir ;
- Symphonic Gospel ;
- Gospel Jam ;
- Black Odyssée ;
- Soul & Jazz ;
- Ebano Nala ;
- Akpade ;
- Les Petites Voix Pop.

Je ne reprendrai aucune information de ces formations.

## Questionnaire à remplir (ou documents à m'envoyer)

| # | Information | Obligatoire | Réponse |
|---|---|---|---|
| 1 | Nom officiel exact (orthographe, majuscules, accents) | ✅ | |
| 2 | Date de création et ville de rattachement | ✅ | |
| 3 | Nature : groupe de scène (concerts, événements) ou ensemble participatif (chœur ouvert à recrutement) ? | ✅ (détermine la page et le Schema) | |
| 4 | Concept en 2-3 phrases : ce qui le rend unique | ✅ | |
| 5 | Styles musicaux et répertoire (titres ou types de répertoire) | ✅ | |
| 6 | Votre rôle : direction artistique, chant lead, arrangements… | ✅ | |
| 7 | Formation : nombre de membres et instruments | ✅ | |
| 8 | Membres : noms publiables ? Avec un accord écrit de chacun ? | si nominatif | |
| 9 | Public visé : particuliers (mariages, événements), entreprises, salles, festivals, choristes à recruter | ✅ | |
| 10 | Concerts passés et à venir (dates **confirmées** uniquement) | — | |
| 11 | Prestations proposées et modalités de réservation (sans tarifs inventés) | — | |
| 12 | Recrutement ou participation : conditions, niveau, répétitions (lieu, fréquence) | si applicable | |
| 13 | Photos officielles : fichiers, crédit photographe, droits d'usage, accord des personnes visibles | ✅ (au moins 1) | |
| 14 | Vidéos et audio (YouTube, SoundCloud…) | — | |
| 15 | Réseaux sociaux du groupe (URL) | — | |
| 16 | Contact : formulaire du site, e-mail dédié, Calendly ? | ✅ | |
| 17 | Lien avec vos autres activités à mettre en avant (chorale, coaching, festival) | — | |

## Ce que je préparerai ensuite (en brouillon)

- **Slug** : `/<nom-du-groupe>/`, ou rattachée à `/sabine-kouli-concerts-groupes/<nom>/` comme les autres formations, pour rester cohérent avec l'arborescence existante (Spectacles).
- **Plan de la page** :
  1. H1 = nom officiel ;
  2. introduction ;
  3. Concept et identité musicale ;
  4. Répertoire ;
  5. Direction artistique / Les musiciens ;
  6. Photos et vidéos ;
  7. Actualités et prochains concerts ;
  8. Réserver, participer ou contacter ;
  9. CTA ;
  10. liens vers vos autres activités.
- **Schema** : si c'est une formation de scène, `MusicGroup`, avec `@id` dédié, `founder` ou `member` → `#person` de Sabine Kouli (uniquement les membres autorisés), `genre`, `sameAs` (réseaux du groupe). `MusicEvent` seulement pour des dates réelles. Le tout ajouté au graphe Yoast par le même filtre que le Schema local (pas de second bloc JSON-LD).
- Titre SEO, méta-description, ALT : rédigés une fois les informations reçues.
