# Utilise l'image hello-world comme image de base
FROM hello-world:latest

# Définit une variable d'environnement (optionnel)
ENV MESSAGE="Hello, custom Docker image!"

# Modifie le comportement par défaut pour afficher un message personnalisé
CMD echo "$MESSAGE"
