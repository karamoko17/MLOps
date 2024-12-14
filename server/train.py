# train.py
import joblib
import numpy as np
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score, roc_curve, auc, precision_recall_curve


# Charger les données Iris
data = load_iris()
X, y = data.data, data.target
feature_names = data.feature_names

# Diviser en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42, stratify=y)

# Entraîner un modèle knn
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)


# Évaluer le modèle
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

#le rapport de classification
print(classification_report(y_test, y_pred, target_names=data.target_names))


# Calculer la courbe ROC et l'AUC
fpr, tpr, _ = roc_curve(y_test, y_prob[:, 1], pos_label=1)  # Choisir la classe positive (par exemple classe 1)
roc_auc = auc(fpr, tpr)

# Calculer la courbe Precision-Recall et l'AUC
precision, recall, _ = precision_recall_curve(y_test, y_prob[:, 1])
pr_auc = auc(recall, precision)

# Afficher les résultats
print(f"AUC ROC: {roc_auc:.2f}")
print(f"AUC PR: {pr_auc:.2f}")


# Sauvegarder le modèle dans un fichier .pkl
joblib.dump(model, "./model.pkl")
joblib.dump(feature_names, "./feature_names.pkl")
print("Model and feature names saved as 'model.pkl'.")



# Sauvegarder les métriques dans un fichier
metrics = {
    "accuracy": accuracy,
    "classification_report": classification_report(y_test, y_pred, target_names=data.target_names),
    "roc_auc": roc_auc,
    "fpr": fpr,
    "tpr": tpr,
    "pr_auc": pr_auc,
    "precision": precision,
    "recall": recall
}

# Sauvegarder les métriques dans un fichier avec joblib
joblib.dump(metrics, "./metrics.pkl")

print("Model, feature names, and metrics saved.")