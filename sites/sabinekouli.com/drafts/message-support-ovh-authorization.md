# Message au support OVH (à envoyer depuis l'espace client : Aide > Créer un ticket)

Objet : En-tête HTTP « Authorization » non transmis à PHP – hébergement sabinekouli.com

Bonjour,

Sur mon hébergement web qui héberge le site WordPress sabinekouli.com, l'en-tête HTTP « Authorization » (authentification Basic) n'est pas transmis à PHP.

Conséquence : les « mots de passe d'application » de WordPress (authentification de l'API REST) ne fonctionnent pas. Toute requête authentifiée vers https://sabinekouli.com/wp-json/wp/v2/users/me répond « 401 rest_not_logged_in », y compris avec des identifiants valides envoyés depuis mon propre ordinateur.

J'ai déjà ajouté en tête du fichier .htaccess, sans effet :
SetEnvIf Authorization "(.*)" HTTP_AUTHORIZATION=$1
RewriteRule .* - [E=HTTP_AUTHORIZATION:%{HTTP:Authorization}]

Pourriez-vous :
1. vérifier si l'en-tête Authorization est retiré en amont (frontal, proxy ou configuration PHP-FPM) sur mon hébergement ;
2. m'indiquer la configuration à appliquer pour qu'il parvienne à PHP (par exemple « CGIPassAuth On » dans .htaccess, ou un réglage du fichier .ovhconfig) ;
3. me préciser mon offre d'hébergement et si l'accès SSH y est disponible.

Merci d'avance,
Sabine Kouli
