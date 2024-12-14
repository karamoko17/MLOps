import threading
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import streamlit as st
import requests
from pydantic import BaseModel
import joblib
import os

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


# FastAPI App
fastapi_app = FastAPI()

# Autoriser les requêtes CORS pour Streamlit
fastapi_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Schéma pour les requêtes de prédiction
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


@fastapi_app.get("/metrics/")
def get_metrics():
    # Renvoyer les métriques sous forme de dictionnaire
    return {
        "accuracy": metrics["accuracy"],
        "roc_auc": metrics["roc_auc"],
        "pr_auc": metrics["pr_auc"],
        "classification_report": metrics["classification_report"],
    }


# Fonction pour démarrer FastAPI
def start_fastapi():
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)


# Streamlit App
def start_streamlit():
    st.title("MLOps Dashboard")
    st.write("Interagissez avec le modèle FastAPI à l'aide de cette interface.")

    # Formulaire de prédiction
    st.subheader("Faire une prédiction")
    sepal_length = st.number_input("Longueur du sépale", min_value=0.0)
    sepal_width = st.number_input("Largeur du sépale", min_value=0.0)
    petal_length = st.number_input("Longueur du pétale", min_value=0.0)
    petal_width = st.number_input("Largeur du pétale", min_value=0.0)

    if st.button("Prédire"):
        payload = {
            "sepal_length": sepal_length,
            "sepal_width": sepal_width,
            "petal_length": petal_length,
            "petal_width": petal_width,
        }
        response = requests.post("http://localhost:8000/predict/", json=payload)
        if response.status_code == 200:
            st.success(f"Résultat : {response.json()['prediction']}")
        else:
            st.error("Erreur lors de la requête à l'API")

    # Visualisation des métriques
    st.subheader("Visualiser les métriques")
    if st.button("Obtenir les métriques"):
        response = requests.get("http://localhost:8000/metrics/")
        if response.status_code == 200:
            metrics = response.json()
            st.json(metrics)
        else:
            st.error("Erreur lors de la récupération des métriques")


# Lancer FastAPI et Streamlit ensemble
if __name__ == "__main__":
    # Démarrer FastAPI dans un thread séparé
    api_thread = threading.Thread(target=start_fastapi, daemon=True)
    api_thread.start()

    # Lancer Streamlit
    start_streamlit()
