# Restaurant Sales Prediction (MLOps Deployment)

This project demonstrates an end-to-end MLOps workflow by deploying a Machine Learning model using a Streamlit web application, containerized with Docker for seamless scalability and portability.

## Project Structure
- `app.py`: The Streamlit web interface and model inference logic.
- `train_model.py`: Script to generate the machine learning model.
- `model.pkl`: The serialized machine learning model (generated via training).
- `Dockerfile`: Configuration for building the application container.
- `requirements.txt`: Python package dependencies.
- `.dockerignore`: Files to exclude from the Docker container (keeps the image clean).
- `README.md`: Project documentation.

## Prerequisites
Ensure you have Python installed on your system.

## 1. Setup Environment
Install the required dependencies:
``` bash
pip install -r requirements.txt
```

## 2. Train the Model
Before running the application, you must generate the `model.pkl` file. Run the following command:
``` bash
python train_model.py
```
*This will create a `model.pkl` file in your root directory.*

## 3. Run Locally
Once the model is generated, launch the application locally:
``` bash
streamlit run app.py
```
Access the application at `http://localhost:8501`.

## 4. Docker Deployment
Follow these steps to package and run the application as a container:

### Build the Image
``` bash
docker build -t restaurant-sales-app .
```

### Run the Container
``` bash
docker run -p 8501:8501 restaurant-sales-app
```
Access the application at `http://localhost:8501` in your web browser.

## Author
**Animesh Sanghi** | *Google Certified Data Analyst*
[LinkedIn](https://www.linkedin.com/in/animeshsanghi)

## License
This project is open-source and free to use.