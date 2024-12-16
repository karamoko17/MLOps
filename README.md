# Iris Prediction App


## 📖 **Table of Contents**
1. [Descriptions](#descriptions)
2. [Prerequisites](#Prerequisites)
3. [Installation](#Installation)
4. [Features](#Features)
5. [Use and examples of results](#Use-and-examples-of-results)
6. [Deploying the application on Streamlit Cloud](#Deploying-the-application-on-Streamlit-Cloud)
7. [Contribution](#Contribution)
8. [Author](#Author)

<h2 id="Descriptions">🧩 Descriptions</h2>

This application predicts Iris flower species using a machine learning model trained on the Iris dataset. It classifies a flower into one of three species: Setosa, Versicolor, or Virginica, based on its physical characteristics, such as the length and width of the sepals and petals.

The project uses FastAPI to expose an API capable of handling prediction requests via HTTP requests. An interactive user interface has been developed with Streamlit, enabling users to enter the characteristics of a flower and obtain an immediate prediction. To simplify deployment and improve scalability, the entire project is orchestrated in a Dockerized environment.

On the backend, the application integrates with MongoDB to manage data storage, offering functionalities such as adding and listing fruits, illustrating basic interactions with a database.

The machine learning model used is the KNeighborsClassifier, a supervised algorithm based on the k-nearest neighbors (k-NN) method. This model was trained on the Iris dataset, a well-known dataset containing information on 150 flower samples, with four features per sample (length/width of sepals and petals). 

The application allows the user to :

- Enter the characteristics of an Iris flower.
- Get an instant prediction of the flower species.
- View results in text and image format for different species (Setosa, Versicolor, Virginica).
- View model metrics.

<h2 id="Prerequisites">🤖 Prerequisites</h2>

- Docker, Docker Compose and Docker Desktop installed on your machine.
- Python 3.8 or higher
- pip (to install dependencies)
- A virtual environment (optional but recommended)

<h2 id="Installation">🛠️ Installation</h2>

To run this project, follow the steps below:
1. Clone the repository
- Run the following command in your terminal to clone the GitHub repository:
```bash
git clone https://github.com/karamoko17/Projet_MlOps.git
```

2. Access the project directory
- Navigate to the cloned directory:
```bash
cd Projet_MlOps
```

3. Build and start Docker containers
- Run the following command to create the Docker images and start the containers:
```bash
docker-compose up --build  
```

4. Accessing the application
- To access the application, open your browser and enter the following URL:
```bash
http://localhost:8501/
```

You're ready to use the project! 🚀


<h2 id="Features">🏗️ Features</h2>

- Interactive interface via Streamlit
- Prediction of Iris flower species (Setosa, Versicolor, Virginica)
- Display of model metrics
- Visualization of ROC and Precision-Recall curves

<h2 id="Use-and-examples-of-results">💻 Use and examples of results</h2>

The application offers two main interfaces: a Prediction Page, dedicated to the classification of Iris flowers, and a Metrics Page, which visualizes the model's performance.

- **Prediction Page**: This page allows the user to enter the characteristics of a flower, such as the length and width of its sepals and petals. Once the data has been entered, simply click on the Predict button to obtain the result. For example, for specific characteristics, the model can predict that the flower's species is Setosa. In addition, an image illustrating the predicted species is displayed, providing a clear and intuitive visualization of the result.
- **Metrics page**: This page presents model performance via indicators such as accuracy, classification ratio, as well as ROC and Precision-Recall curves. These visualizations make it easy to assess the quality of the model's predictions.

![image](https://github.com/user-attachments/assets/31e87730-aaec-4e3f-99f5-07015e33ceb1)

![image](https://github.com/user-attachments/assets/f98b4f91-bc38-4d6d-9f20-ad40c0bb18be)

![image](https://github.com/user-attachments/assets/190b0859-fc25-4d15-ba4f-74527b0a6c6d)

![image](https://github.com/user-attachments/assets/443a536d-b2ed-4e33-9db9-a9f232017d63)

![image](https://github.com/user-attachments/assets/7f14346a-5ced-495a-8b1c-0fac446f7d0f)


<h2 id="Deploying-the-application-on-Streamlit-Cloud">⚖️ Deploying the application on Streamlit Cloud</h2>

The application has been deployed on **Streamlit Cloud**, offering an interactive interface accessible via the following link: [Access the application](https://irispredictionappawakaramoko.streamlit.app/) or [https://projetmlops-bhfw3yjbjylgdhn8jbrus4.streamlit.app/](https://irispredictionappawakaramoko.streamlit.app/). 

With this deployment, users can easily interact with the application to make predictions on Iris flowers, view results as images and consult model metrics. Streamlit Cloud makes the application available online, without the need for complex infrastructure, offering a fluid user experience accessible from any browser.

<h2 id="Contribution">🤝 Contribution</h2>

Contributions are welcome! Feel free to open a ticket or submit a pull request to suggest improvements. Here's how you can get involved:

1. Clone the project.
2. Create a branch for your feature.
3. Make your changes and validate them with a clear message.
4. Push your changes to your branch on the remote repository.  
5. Submit a pull request to have your contribution reviewed.

<h2 id="Author">🎯 Author</h2> 
This project was designed and developed by KARAMOKO Awa, a student in Master 2 SISE (Statistics and Computer Science for Data Science) at Université Lumière Lyon 2.
