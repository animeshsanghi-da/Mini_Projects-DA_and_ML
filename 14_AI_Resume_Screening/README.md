# AI Resume Screening

This project implements an automated Resume Screening system using Natural Language Processing (NLP) and Machine Learning. It classifies resumes into specific categories (e.g., Data Scientist, Web Developer, HR Specialist, Advocate) based on their content, helping streamline the recruitment process.

## Features

* **Text Preprocessing:** Robust cleaning pipeline to remove URLs, hashtags, mentions, special characters, and non-ASCII text.
* **Feature Extraction:** Utilizes TF-IDF (Term Frequency-Inverse Document Frequency) to convert unstructured text into numerical data for machine learning models.
* **Classification:** Implements the K-Nearest Neighbors (KNN) algorithm to predict categories based on learned patterns.
* **Model Persistence:** Features built-in serialization using `joblib` to save the trained model and vectorizer, allowing for rapid inference without retraining.

## Project Structure

* `resume_dataset.csv`: The dataset containing raw resume text and their respective categories.
* `resume_screening.ipynb`: A Jupyter Notebook containing the initial experiment, data exploration, and model evaluation steps.
* `resume_screening.py`: A production-ready Python script for training the model and performing batch or single predictions.

## Requirements

You will need Python 3.x installed along with the following libraries:

```
pip install pandas scikit-learn joblib
```

## Usage

### 1. Training the Model
To train the model and generate the necessary pickle files for production:

```
python resume_screening.py
```

This will read `resume_dataset.csv`, process the data, train the KNN classifier, and create `tfidf_vectorizer.pkl` and `resume_model.pkl` in your local directory.

### 2. Making Predictions
The `predict_resume(text)` function inside `resume_screening.py` can be imported or called to classify new, unseen resumes:

```
from resume_screening import predict_resume

new_resume = "Expert in Python, machine learning, and deep learning models."
category = predict_resume(new_resume)
print(f"Predicted Category: {category}")
```

## Workflow Explanation

1.  **Cleaning:** The `clean_resume` function normalizes input text by removing noise (special characters, URLs) and converting it to lowercase.
2.  **Vectorization:** The `TfidfVectorizer` learns the vocabulary from the training set and transforms resumes into a sparse matrix of TF-IDF scores.
3.  **Classification:** `KNeighborsClassifier` finds the closest samples in the feature space to the input resume and assigns the majority category.
4.  **Deployment:** By using `joblib`, the model state is preserved, enabling lightweight prediction scripts that can be integrated into web applications or automated pipelines.

## Author
**Animesh Sanghi** | *Google Certified Data Analyst*  
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com

## License

This project is open-source and free to use.