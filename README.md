# Iris Prediction App

## 📖 **Table of Contents**
1. [Descriptions](#descriptions)
2. [Prerequisites](#Prerequisites)
3. [Installation](#Installation)
4. [Usage](#Usage)
5. [Features](#Features)
6. [Sample Results](#Sample-Results)
7. [Deploying the App on Streamlit Cloud](#Deploying-the-App-on-Streamlit-Cloud)

<h2 id="Description">🧩Description</h2>

This app predicts Iris flower species using a machine learning model previously trained on the Iris dataset. The model is able to classify a flower into three possible species: Setosa, Versicolor, or Virginica, based on its physical characteristics, such as the length and width of the sepals and petals.

The project uses FastAPI to expose an API, allowing prediction requests to be processed via HTTP requests. Streamlit is used to create an interactive graphical interface, where the user can easily enter the characteristics of a flower and get an immediate prediction.

The machine learning model used in this project is a supervised model that was trained using the Iris dataset. This database is widely used for machine learning classification demonstrations and contains information on 150 samples of Iris flowers, with four features per sample.

The application allows the user to:

- Enter the characteristics of an Iris flower.
- Get an instant prediction on the species of the flower.
- Visualize the results in the form of text and images of the different species (Setosa, Versicolor, Virginica).
- View model metrics such as accuracy, classification ratio, ROC and Precision-Recall curves.

<h2 id="Prerequisites">🤖 Prerequisites</h2>

- Docker and Docker Compose installed on your machine.
-Python 3.8 or higher
- pip (for dependency installation)
- A virtual environment (optional but recommended)

<h2 id="Installation">🛠️Installation</h2>

``` bash
- Clone the repository
clone git [https://github.com/username/iris-flower-prediction.git](https://github.com/karamoko17/Projet_MlOps.git)
cd iris-fleur-prédiction

- Create a virtual environment (optional)
python3 -m venv venv
source venv/bin/activate # On Windows, use venv\Scripts\activate

- Install dependencies
pip install -r requirements.txt
```

<h2 id="Usage">💻Usage</h2>

``` bash
Docker compose build
Docker compose

# Start the API FastAPI
Uvicorne application: application --reload

# Start the Streamlit application
simplified execution app.py
or
http://localhost:8501/

an example of an input for the API:
{
"sepal_length": 5.1,
"sepal_width": 3.5,
"petal_length": 1.4,
"petal_width": 0.2
}
```

<h2 id="Features">🏗️ Features</h2>

- Prediction of Iris flower species (Setosa, Versicolor, Virginica)
- Display of model metrics
- Visualization of ROC and Precision-Recall curves
- Interactive interface via Streamlit

<h2 id="Example results">🎯 Example results</h2>

The application offers two main interfaces: a page dedicated to the prediction of Iris flower species and another for displaying model metrics.

Feature example:

- **Prediction**: The user enters the characteristics of a flower and the model predicts the species. For example, the prediction for a given flower could be Setosa.
- **Flower Image**: An image of the flower corresponding to the prediction is displayed, providing a visual representation.
- **Metrics**: Model metrics, such as accuracy, classification ratio, and ROC and Precision-Recall curves, are displayed to evaluate the model's performance.

![image](https://github.com/user-attachments/assets/31e87730-aaec-4e3f-99f5-07015e33ceb1)

![image](https://github.com/user-attachments/assets/f98b4f91-bc38-4d6d-9f20-ad40c0bb18be)

![image](https://github.com/user-attachments/as ensembles/190b0859-fc25-4d15-ba4f-74527b0a6c6d)

![image](https://github.com/user-attachments/assets/443a536d-b2ed-4e33-9db9-a9f232017d63)

![image](https:// github.com/user-attachments/assets/7f14346a-5ced-495a-8b1c-0fac446f7d0f)

<h2 id="Deploying the application on Streamlit Cloud">⚖️ Deploying the application on Streamlit Cloud</h2>

The application has been deployed on **Streamlit Cloud**, providing an interactive interface accessible via the following link: [Access the application](https://projetmlops-bhfw3yjbjylgdhn8jbrus4.streamlit.app/) or https:/ /projetmlops-bhfw3yjbjylgdhn8jbrus4.streamlit.app/.

With this deployment, users can easily interact with the application to make predictions about Iris flowers, visualize the results as images, and view model metrics. Streamlit Cloud makes the application available online, without the need for complex infrastructure, providing a seamless user experience that can be accessed from any browser.
