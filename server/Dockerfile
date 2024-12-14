FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY app.py app.py
# Copier les scripts et modèles
COPY model.pkl model.pkl
COPY feature_names.pkl feature_names.pkl
COPY metrics.pkl /app/metrics.pkl

# Exposer le port 8000
EXPOSE 8000

# Lancer le serveur FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]