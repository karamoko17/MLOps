import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, roc_curve, auc
from sklearn.preprocessing import label_binarize

# Charger les données Iris
data = load_iris()
X, y = data.data, data.target
feature_names = data.feature_names

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42, stratify=y)

# Entraîner un modèle KNN
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# Prédictions et probabilités
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)

# Calculer les performances
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
print(classification_report(y_test, y_pred, target_names=data.target_names))

# ---- Precision-Recall pour chaque classe ----
y_test_bin = label_binarize(y_test, classes=[0, 1, 2])  # Binarisation des classes (Setosa, Versicolor, Virginica)
n_classes = y_test_bin.shape[1]

# Plot des courbes Precision-Recall pour chaque classe
plt.figure(figsize=(10, 8))
for i in range(n_classes):
    precision, recall, _ = precision_recall_curve(y_test_bin[:, i], y_prob[:, i])
    plt.plot(recall, precision, label=f'Classe {data.target_names[i]}')

plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Courbes Precision-Recall pour chaque classe')
plt.legend(loc="best")
plt.grid(True)
plt.show()

# ---- ROC pour chaque classe ----
fpr = dict()
tpr = dict()
roc_auc = dict()

for i in range(n_classes):
    fpr[i], tpr[i], _ = roc_curve(y_test_bin[:, i], y_prob[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

# Tracer les courbes ROC
plt.figure(figsize=(10, 8))
for i in range(n_classes):
    plt.plot(fpr[i], tpr[i], label=f'Classe {data.target_names[i]} (AUC = {roc_auc[i]:.2f})')

plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Courbe ROC pour chaque classe')
plt.legend(loc='best')
plt.grid(True)
plt.show()

# Sauvegarder le modèle et les fichiers nécessaires
joblib.dump(model, '/app/models/model.pkl')
#joblib.dump(feature_names, "/app/models/feature_names.pkl")
print("Model and feature names saved as 'model.pkl'.")
