# Sauvegarde complète vers Google Drive avec UpdraftPlus

Pour : sabinekouli.com, et tout autre site WordPress du projet (un réglage par site).
Opération à faire **par vous** dans l'administration WordPress, avec un compte administrateur : installer une extension est un changement de niveau 3, validé le 24/11/2026.

## Pourquoi UpdraftPlus

- Gratuit, très répandu, et il sauvegarde **tout ce que l'export public ne peut pas récupérer** : base de données (réglages, métadonnées Yoast, menus, widgets, utilisateurs, formulaires, brouillons), thème, extensions, médias et autres fichiers.
- Sauvegardes automatiques planifiées, envoyées directement sur votre Google Drive.
- Restauration en quelques clics depuis l'administration.

## Étapes (environ 10 minutes)

1. **Installer** : *Extensions > Ajouter*, recherchez « UpdraftPlus », choisissez **UpdraftPlus: WP Backup & Migration Plugin** (éditeur : TeamUpdraft), puis *Installer* et *Activer*.
2. **Ouvrir** : *Réglages > Sauvegardes UpdraftPlus*, onglet **Réglages**.
3. **Planification** :
   - Fichiers : **Hebdomadaire**, conserver **4** sauvegardes.
   - Base de données : **Quotidienne**, conserver **14** sauvegardes.
4. **Stockage distant** : cliquez sur l'icône **Google Drive**.
5. **Inclure** : Extensions, Thèmes, Téléversements, Autres (tout cocher).
6. **Enregistrer les modifications** en bas de page. Une fenêtre propose un lien d'autorisation : connectez-vous avec **votre** compte Google, acceptez, puis cliquez sur **Complete setup**.
7. **Première sauvegarde** : onglet *Sauvegarde / Restauration* > **Sauvegarder maintenant**. Cochez « inclure la base de données », « inclure les fichiers » et « envoyer vers le stockage distant ».
8. **Vérifier** : dans Google Drive, un dossier **UpdraftPlus** contient des fichiers `backup_AAAA-MM-JJ-…`. Il doit y en avoir 5 types : `-db.gz`, `-plugins.zip`, `-themes.zip`, `-uploads.zip`, `-others.zip`. Envoyez-moi une capture ou la liste des noms, et je consignerai la vérification.

## Bonnes pratiques

- **Ne partagez pas** le dossier UpdraftPlus : la base de données contient les adresses e-mail des comptes et des mots de passe chiffrés.
- Avant chaque intervention importante (lot de corrections SEO, migration d'articles), lancez une sauvegarde manuelle (étape 7).
- Une fois par trimestre, vérifiez qu'une sauvegarde récente est bien présente dans Drive.
- Les sauvegardes automatiques d'OVH restent un filet de sécurité complémentaire.
- En cas d'échec à l'envoi (hébergement mutualisé et gros fichiers) : UpdraftPlus découpe les archives automatiquement. Si l'erreur persiste, envoyez-moi le journal (*Sauvegarde / Restauration > Journal*).

## Restauration (pour mémoire)

*Sauvegarde / Restauration > Sauvegardes existantes > Restaurer*, puis cocher les éléments à restaurer. Ne restaurez jamais sans m'en parler, sauf en cas d'urgence.

## Export de contenu complémentaire (déjà fait le 24/11/2026)

`scripts/export_public.py` a produit une archive de référence (contenu, HTML publié, médias), qui ne permet pas de restaurer le site.
Elle n'a pas pu être envoyée sur Google Drive depuis la session cloud : le connecteur limite chaque envoi à environ 3 Mo.
UpdraftPlus rend cette archive secondaire.
