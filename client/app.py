import streamlit as st
import requests
import joblib
import pandas as pd
import matplotlib.pyplot as plt

# Charger les métriques sauvegardées (assure-toi que 'metrics.pkl' est dans le bon répertoire)
metrics = joblib.load("metrics.pkl") 

# URL de l'API FastAPI
API_URL = "http://server:8000/predict/"

st.title("Welcome to My App: Iris Flower Predictor")

# Initialiser l'état de la page si nécessaire
if "current_page" not in st.session_state:
    st.session_state.current_page = "Prédiction"  # Page par défaut


# ---------------------- Page de Prédiction ----------------------
def prediction_page():
    st.title("Iris Flower Predictor")
    st.write("Entrez les caractéristiques de la fleur pour prédire sa catégorie.")

    # Interface utilisateur pour la prédiction
    sepal_length = st.number_input("Sepal Length", min_value=0.0, step=0.1)
    sepal_width = st.number_input("Sepal Width", min_value=0.0, step=0.1)
    petal_length = st.number_input("Petal Length", min_value=0.0, step=0.1)
    petal_width = st.number_input("Petal Width", min_value=0.0, step=0.1)

    if st.button("Prédire"):
        if sepal_length == 0.0 and sepal_width == 0.0 and petal_length == 0.0 and petal_width == 0.0:
            st.error("Veuillez entrer des valeurs non nulles pour les caractéristiques de la fleur.")
        else:
            # Préparer les données pour la requête
            payload = {
                "sepal_length": sepal_length,
                "sepal_width": sepal_width,
                "petal_length": petal_length,
                "petal_width": petal_width,
            }

            try:
                # Envoyer la requête POST
                response = requests.post(API_URL, json=payload)

                # Vérifier si la réponse est valide
                if response.status_code == 200:
                    response_data = response.json()
                    if "prediction" in response_data:
                        prediction = response_data["prediction"]
                        st.success(f"La fleur prédite est : **{prediction}**")

                        # Afficher l'image de la fleur prédite
                        if prediction == "Setosa":
                            st.image("images/setosa.jpg", caption="Iris Setosa", use_container_width=True)
                        elif prediction == "Versicolor":
                            st.image("images/versicolor.jpg", caption="Iris Versicolor", use_container_width=True)
                        elif prediction == "Virginica":
                            st.image("images/virginica.jpg", caption="Iris Virginica", use_container_width=True)
                    else:
                        st.error(f"Réponse de l'API inattendue : {response_data}")
                else:
                    st.error(f"Erreur API ({response.status_code}): {response.text}")

            except requests.exceptions.RequestException as e:
                st.error(f"Erreur de connexion à l'API : {e}")






# ---------------------- Page des Métriques ----------------------
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
if st.sidebar.button("Page Prédiction"):
    st.session_state.current_page = "Prédiction"

if st.sidebar.button("Page Métriques"):
    st.session_state.current_page = "Métriques"

# Afficher la page en fonction de l'état
if st.session_state.current_page == "Prédiction":
    prediction_page()
elif st.session_state.current_page == "Métriques":
    metrics_page()