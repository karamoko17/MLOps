FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt 

RUN pip install -r requirements.txt

COPY app.py app.py 
COPY images/ /app/images/
COPY metrics.pkl /app/metrics.pkl


EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]