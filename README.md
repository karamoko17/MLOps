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

L'application propose deux interfaces principales : une page dédiée à la prédiction des espèces de fleurs Iris et une autre pour l'affichage des métriques du modèle.

Exemple de fonctionnalité :

- Prédiction : L'utilisateur entre les caractéristiques d'une fleur et le modèle prédit l'espèce. Par exemple, la prédiction pour une fleur donnée pourrait être Setosa.
- Image de la fleur : Une image de la fleur correspondant à la prédiction est affichée, offrant une représentation visuelle.
- Métriques : Les métriques du modèle, telles que la précision, le rapport de classification, et les courbes ROC et Precision-Recall, sont affichées pour évaluer la performance du modèle.

![image](https://github.com/user-attachments/assets/31e87730-aaec-4e3f-99f5-07015e33ceb1)

![image](https://github.com/user-attachments/assets/f98b4f91-bc38-4d6d-9f20-ad40c0bb18be)

![image](https://github.com/user-attachments/assets/190b0859-fc25-4d15-ba4f-74527b0a6c6d)

![image](https://github.com/user-attachments/assets/443a536d-b2ed-4e33-9db9-a9f232017d63)

![image](https://github.com/user-attachments/assets/7f14346a-5ced-495a-8b1c-0fac446f7d0f)


<h2 id="Deployememnt de l'appliction sur Streamlit Cloud">⚖️ Deployememnt de l'appliction sur Streamlit Cloud</h2>

L'application a été déployée sur Streamlit Cloud, offrant ainsi une interface interactive accessible via le lien suivant: https://projetmlops-bhfw3yjbjylgdhn8jbrus4.streamlit.app/.

Grâce à ce déploiement, les utilisateurs peuvent facilement interagir avec l'application pour effectuer des prédictions sur les fleurs Iris, visualiser les résultats sous forme d'images et consulter les métriques du modèle. Streamlit Cloud permet de rendre l'application disponible en ligne, sans nécessiter d'infrastructure complexe, offrant ainsi une expérience utilisateur fluide et accessible depuis n'importe quel navigateur.
