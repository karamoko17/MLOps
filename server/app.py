from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Charger le modèle KNN
model = joblib.load("model.pkl")
feature_names = joblib.load("feature_names.pkl")  # Si tu veux utiliser les noms des caractéristiques
metrics = joblib.load("metrics.pkl")


app = FastAPI()

# Schéma pour les requêtes de prédiction
class PredictionRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict/")
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

@app.get("/metrics/")
def get_metrics():
    # Renvoyer les métriques sous forme de dictionnaire
    return {
        "accuracy": metrics["accuracy"],
        "roc_auc": metrics["roc_auc"],
        "pr_auc": metrics["pr_auc"],
        "classification_report": metrics["classification_report"],
        "fpr": metrics["fpr"].tolist(),  # Convertir en liste pour pouvoir sérialiser
        "tpr": metrics["tpr"].tolist(),  # Convertir en liste pour pouvoir sérialiser
        "precision": metrics["precision"].tolist(),  # Convertir en liste pour pouvoir sérialiser
        "recall": metrics["recall"].tolist(),  # Convertir en liste pour pouvoir sérialiser
    }