# Utilise une image de base Python
FROM python:3.9-slim

# Définir le répertoire de travail dans le container
WORKDIR /app

# Copier les fichiers nécessaires dans le container
COPY requirements.txt /app/requirements.txt
COPY train.py /app/train.py

# Installer les dépendances
RUN pip install -r requirements.txt

# Commande pour exécuter train.py
CMD ["python", "train.py"]
