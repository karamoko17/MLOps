import os
#import threading
import requests
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel
import requests


# Charger les ressources nécessaires pour le serveur FastAPI
#model = joblib.load("server/model.pkl")
#metrics = joblib.load("server/metrics.pkl")
#feature_names = joblib.load("server/feature_names.pkl")

# Définir un chemin absolu basé sur le répertoire racine
file_path = os.path.join("server", "metrics.pkl")
metrics = joblib.load(file_path)

# Définir un chemin absolu basé sur le répertoire racine
file_path1 = os.path.join("server", "model.pkl")
model = joblib.load(file_path1)

# Définir un chemin absolu basé sur le répertoire racine
file_path2 = os.path.join("server", "feature_names.pkl")
feature_names = joblib.load(file_path2)


# ---------------------------------------------
# Configuration FastAPI
# ---------------------------------------------
fastapi_app = FastAPI()

# Autoriser les requêtes CORS pour Streamlit
fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permettre les requêtes de toutes origines
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Schéma pour la requête de prédiction
class PredictionRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


@fastapi_app.post("/predict/")
def predict(request: PredictionRequest):
    input_data = [
        request.sepal_length,
        request.sepal_width,
        request.petal_length,
        request.petal_width,
    ]
    prediction = model.predict([input_data])[0]
    class_name = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
    return {"prediction": class_name[prediction]}



# Fonction pour démarrer FastAPI
def start_fastapi():
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)


# ---------------------------------------------
# Configuration Streamlit
# ---------------------------------------------
# URL de l'API FastAPI
API_URL = "http://localhost:8000"
API_URL1 = "http://fastapi:8000/predict/"
# Fonction pour afficher la page de prédiction
def prediction_page():
    st.title("Welcome to My App: Iris Flower Predictor")
    st.write("Entrez les caractéristiques de la fleur pour prédire sa catégorie.")

    # Champs de saisie pour la prédiction
    sepal_length = st.number_input("Sepal Length", min_value=0.0, step=0.1)
    sepal_width = st.number_input("Sepal Width", min_value=0.0, step=0.1)
    petal_length = st.number_input("Petal Length", min_value=0.0, step=0.1)
    petal_width = st.number_input("Petal Width", min_value=0.0, step=0.1)

    if st.button("Prédire"):
        if all(v == 0.0 for v in [sepal_length, sepal_width, petal_length, petal_width]):
            st.error("Veuillez entrer des valeurs non nulles pour les caractéristiques.")
        else:
            payload = {
                "sepal_length": sepal_length,
                "sepal_width": sepal_width,
                "petal_length": petal_length,
                "petal_width": petal_width,
            }
            try:
                # Envoyer la requête POST
                response = requests.post(API_URL1, json=payload)

                # Vérifier si la réponse est valide
                if response.status_code == 200:
                    response_data = response.json()
                    if "prediction" in response_data:
                        prediction = response_data["prediction"]
                        st.success(f"La fleur prédite est : **{prediction}**")

                        # Afficher l'image de la fleur prédite
                        if prediction == "Setosa":
                            st.image("client/images/setosa.jpg", caption="Iris Setosa", use_container_width=True)
                        elif prediction == "Versicolor":
                            st.image("client/images/versicolor.jpg", caption="Iris Versicolor", use_container_width=True)
                        elif prediction == "Virginica":
                            st.image("client/images/virginica.jpg", caption="Iris Virginica", use_container_width=True)
                    else:
                        st.error(f"Réponse de l'API inattendue : {response_data}")
                else:
                    st.error(f"Erreur API ({response.status_code}): {response.text}")

            except requests.exceptions.RequestException as e:
                st.error(f"Erreur de connexion à l'API : {e}")


# Fonction pour afficher la page des métriques


def metrics_page():
    st.title("Métriques d'apprentissage du modèle")

    # Afficher les métriques
    st.subheader("Accuracy")
    st.write(f"Accuracy: {metrics['accuracy']:.2f}")

    st.subheader("Classification Report")
    st.text(metrics['classification_report'])

    st.subheader("AUC ROC")
    for i in range(len(metrics['roc_auc'])):
        st.write(f"AUC ROC for class {i}: {metrics['roc_auc'][i]:.2f}")

    # Afficher la courbe ROC pour chaque classe
    st.subheader("Courbe ROC")
    for i in range(len(metrics['roc_auc'])):
        fig, ax = plt.subplots()
        ax.plot(metrics['fpr'][i], metrics['tpr'][i], color='b', lw=2, label=f'ROC curve (area = {metrics["roc_auc"][i]:.2f})')
        ax.plot([0, 1], [0, 1], color='gray', linestyle='--')
        ax.set(xlim=[0.0, 1.0], ylim=[0.0, 1.05], xlabel='False Positive Rate', ylabel='True Positive Rate')
        ax.legend(loc='lower right')
        st.pyplot(fig)

    # Afficher la courbe Precision-Recall pour chaque classe
    st.subheader("Courbe Precision-Recall")
    for i in range(len(metrics['pr_auc'])):
        fig, ax = plt.subplots()
        ax.plot(metrics['recall'][i], metrics['precision'][i], color='b', lw=2, label=f'PR curve (area = {metrics["pr_auc"][i]:.2f})')
        ax.set(xlim=[0.0, 1.0], ylim=[0.0, 1.05], xlabel='Recall', ylabel='Precision')
        ax.legend(loc='lower left')
        st.pyplot(fig)      
        
        
        


# ---------------------- Gestion de la navigation ----------------------
# Ajouter les boutons dans la barre latérale pour changer de page
if "current_page" not in st.session_state:
    st.session_state.current_page = "Prédiction"  # Page par défaut

# Utilisation de st.radio pour la navigation entre les pages
page = st.sidebar.radio("Aller à", ["Prédiction", "Métriques"])

# Mise à jour de la page en fonction de la sélection de l'utilisateur
if page == "Prédiction":
    st.session_state.current_page = "Prédiction"
elif page == "Métriques":
    st.session_state.current_page = "Métriques"

# Afficher la page en fonction de l'état
if st.session_state.current_page == "Prédiction":
    prediction_page()
elif st.session_state.current_page == "Métriques":
    metrics_page()
    
    
