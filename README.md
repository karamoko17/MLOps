# Iris Prediction App


## 📖 **Table of Contents**
1. [Descriptions](#descriptions)
2. [Prérequis](#Prérequis)
3. [Installation](#Installation)
4. [Utilisation](#Utilisation)
5. [Fonctionnalités](#Fonctionnalités)
6. [Exemples de résultats](#Exemples-de-résultats)
7. [Deployememnt de l'appliction sur Streamlit Cloud](#Deployememnt-de-l'appliction-sur-Streamlit-Cloud)

<h2 id="Description">🧩 **Description**</h2>

Cette application permet de prédire les espèces de fleurs Iris à l'aide d'un modèle de machine learning préalablement entraîné sur l'ensemble de données Iris. Le modèle est capable de classer une fleur parmi trois espèces possibles : Setosa, Versicolor, ou Virginica, en fonction de ses caractéristiques physiques, telles que la longueur et la largeur des sépales et des pétales.

Le projet utilise FastAPI pour exposer une API, permettant de traiter les demandes de prédiction via des requêtes HTTP. Streamlit est utilisé pour créer une interface graphique interactive, où l'utilisateur peut facilement entrer les caractéristiques d'une fleur et obtenir une prédiction immédiate.

Le modèle de machine learning utilisé dans ce projet est un modèle supervisé qui a été formé à l'aide de l'ensemble de données Iris. Cette base de données est largement utilisée pour les démonstrations de classification en machine learning et contient des informations sur 150 échantillons de fleurs Iris, avec quatre caractéristiques par échantillon.

L'application permet à l'utilisateur de :

- Entrer les caractéristiques d'une fleur Iris.
- Obtenir une prédiction instantanée sur l'espèce de la fleur.
- Visualiser les résultats sous forme de texte et d'images des différentes espèces (Setosa, Versicolor, Virginica).
- Consulter les métriques du modèle, telles que la précision, le rapport de classification, ainsi que les courbes ROC et Precision-Recall.

<h2 id="Prérequis">🤖 Prérequis</h2>

- Docker et Docker Compose installés sur votre machine.
- Python 3.8 ou supérieur
- pip (pour l'installation des dépendances)
- Un environnement virtuel (facultatif mais recommandé)

<h2 id="Installation">🛠️ Installation</h2>

``` bash
- Clonez le dépôt
git clone [https://github.com/username/iris-flower-prediction.git](https://github.com/karamoko17/Projet_MlOps.git)
cd iris-flower-prediction

- Créez un environnement virtuel (optionnel)
python3 -m venv venv
source venv/bin/activate  # Sur Windows, utilisez venv\Scripts\activate

- Installez les dépendances
pip install -r requirements.txt
```

<h2 id="Utilisation">💻 Utilisation</h2>

``` bash
docker compose build
docker compose up

# Démarrez l'API FastAPI
uvicorn app:app --reload

# Démarrez l'application Streamlit
streamlit run app.py
ou
http://localhost:8501/

un exemple d'input pour l'API:
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

<h2 id="Fonctionnalités">🏗️ Fonctionnalités</h2>

- Prédiction des espèces de fleurs Iris (Setosa, Versicolor, Virginica)
- Affichage des métriques du modèle
- Visualisation des courbes ROC et Precision-Recall
- Interface interactive via Streamlit

<h2 id="Exemples de résultats">🎯 Exemples de résultats</h2>

Voici un exemple de prédiction pour une fleur Iris :
- Prédiction : Setosa
- Image de la fleur
![image](https://github.com/user-attachments/assets/07aa8bfd-87ca-45ed-9852-46a95e2be512)

  


<h2 id="Deployememnt de l'appliction sur Streamlit Cloud">⚖️ Deployememnt de l'appliction sur Streamlit Cloud</h2>

https://projetmlops-bhfw3yjbjylgdhn8jbrus4.streamlit.app/
