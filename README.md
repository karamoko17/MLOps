# Iris Prediction App


## 📖 **Table of Contents**
1. [Descriptions](#descriptions)
2. [Prérequis](#Prérequis)
3. [Installation](#Installation)
4. [Utilisation](#Utilisation)
5. [Fonctionnalités](#Fonctionnalités)
6. [Utilisation et exemples de résultats](#Utilisation-et-exemples-de-résultats)
7. [Deployememnt de l'appliction sur Streamlit Cloud](#Deployememnt-de-l'appliction-sur-Streamlit-Cloud)
8. [Auteur](#Auteur)

<h2 id="Description">🧩 Description</h2>

Cette application prédit les espèces de fleurs Iris à l'aide d'un modèle de machine learning entraîné sur l'ensemble de données Iris. Elle permet de classer une fleur parmi trois espèces : Setosa, Versicolor, ou Virginica, en se basant sur ses caractéristiques physiques, telles que la longueur et la largeur des sépales et des pétales.

Le projet utilise FastAPI pour exposer une API capable de traiter les demandes de prédiction via des requêtes HTTP. Une interface utilisateur interactive a été développée avec Streamlit, permettant aux utilisateurs de saisir les caractéristiques d'une fleur et d'obtenir une prédiction immédiate. Pour simplifier le déploiement et améliorer l'évolutivité, l'ensemble du projet est orchestré dans un environnement Dockerisé.

En backend, l'application s'intègre à MongoDB pour gérer le stockage des données, offrant des fonctionnalités telles que l'ajout et la liste des fruits, illustrant les interactions de base avec une base de données.

Le modèle de machine learning utilisé est le KNeighborsClassifier, un algorithme supervisé basé sur la méthode des k-plus-proches voisins (k-NN). Ce modèle a été formé à partir de l'ensemble de données Iris, un dataset bien connu contenant des informations sur 150 échantillons de fleurs, avec quatre caractéristiques par échantillon (longueur/largeur des sépales et pétales). Ce dataset est largement utilisé dans les démonstrations et expérimentations de classification en machine learning.

L'application permet à l'utilisateur de :

- Entrer les caractéristiques d'une fleur Iris.
- Obtenir une prédiction instantanée sur l'espèce de la fleur.
- Visualiser les résultats sous forme de texte et d'images des différentes espèces (Setosa, Versicolor, Virginica).
- Consulter les métriques du modèle.


<h2 id="Prérequis">🤖 Prérequis</h2>

- Docker et Docker Compose installés sur votre machine.
- Python 3.8 ou supérieur
- pip (pour l'installation des dépendances)
- Un environnement virtuel (facultatif mais recommandé)

<h2 id="Installation">🛠️ Installation</h2>

Pour exécuter ce projet, suivez les étapes ci-dessous :
1. Cloner le dépôt
Exécutez la commande suivante dans votre terminal pour cloner le dépôt GitHub :
```bash
git clone https://github.com/karamoko17/Projet_MlOps.git
```

2. Accéder au répertoire du projet
Naviguez dans le répertoire cloné :
```bash
cd Projet_MlOps
```

3. Construire et démarrer les conteneurs Docker
Exécutez la commande suivante pour créer les images Docker et démarrer les conteneurs :
```bash
docker-compose up --build  
```
Vous êtes prêt à utiliser le projet ! 🚀


<h2 id="Fonctionnalités">🏗️ Fonctionnalités</h2>

- Interface interactive via Streamlit
- Prédiction des espèces de fleurs Iris (Setosa, Versicolor, Virginica)
- Affichage des métriques du modèle
- Visualisation des courbes ROC et Precision-Recall

<h2 id="Utilisation et exemples de résultats">💻 Utilisation et exemples de résultats</h2>

L'application propose deux interfaces principales : une page dédiée à la prédiction (Page Prédiction) des espèces de fleurs Iris et une autre pour l'affichage des métriques du modèle(Page Métriques.

- **Prédiction** : l'utilisateur entre les caractéristiques d'une fleur. Par exemple, la prédiction pour une fleur donnée pourrait être Setosa. Puis cliqué sur le bouton predire.
- **Image de la fleur** : une image de la fleur correspondant à la prédiction est affichée, offrant une représentation visuelle.
- **Métriques** : sur la page Métriques, les métriques du modèle, telles que la précision, le rapport de classification, et les courbes ROC et Precision-Recall, sont affichées pour évaluer la performance du modèle.

![image](https://github.com/user-attachments/assets/31e87730-aaec-4e3f-99f5-07015e33ceb1)

![image](https://github.com/user-attachments/assets/f98b4f91-bc38-4d6d-9f20-ad40c0bb18be)

![image](https://github.com/user-attachments/assets/190b0859-fc25-4d15-ba4f-74527b0a6c6d)

![image](https://github.com/user-attachments/assets/443a536d-b2ed-4e33-9db9-a9f232017d63)

![image](https://github.com/user-attachments/assets/7f14346a-5ced-495a-8b1c-0fac446f7d0f)


<h2 id="Deployememnt de l'appliction sur Streamlit Cloud">⚖️ Deployememnt de l'appliction sur Streamlit Cloud</h2>

L'application a été déployée sur **Streamlit Cloud**, offrant ainsi une interface interactive accessible via le lien suivant: [Accéder à l'application](https://projetmlops-bhfw3yjbjylgdhn8jbrus4.streamlit.app/) ou https://projetmlops-bhfw3yjbjylgdhn8jbrus4.streamlit.app/. 

Grâce à ce déploiement, les utilisateurs peuvent facilement interagir avec l'application pour effectuer des prédictions sur les fleurs Iris, visualiser les résultats sous forme d'images et consulter les métriques du modèle. Streamlit Cloud permet de rendre l'application disponible en ligne, sans nécessiter d'infrastructure complexe, offrant ainsi une expérience utilisateur fluide et accessible depuis n'importe quel navigateur.


<h2 id="Contribution">🤝 Contribution</h2>
Les contributions sont les bienvenues ! N'hésitez pas à ouvrir un ticket ou à soumettre une demande d'extraction pour suggérer des améliorations. Voici comment vous pouvez participer :

1. Clonez le projet.
2. Créez une branche pour votre fonctionnalité.
3. Apportez vos modifications et validez-les avec un message clair.
4. Poussez vos modifications vers votre branche sur le dépôt distant.  
5. Soumettez une pull request pour que votre contribution soit examinée.


<h2 id="Auteur">🎯 Auteur</h2> 
Ce projet a été conçu et développé par KARAMOKO Awa, étudiante en Master 2 SISE (Statistique et Informatique pour la Science des Données) à l'Université Lumière Lyon 2.
