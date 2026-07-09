import pandas as pd
import re
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def clean_resume(resume_text):
    """Cleans the resume text by removing URLs, special characters, and converting to lowercase."""
    resume_text = re.sub('http\S+\s*', ' ', resume_text)
    resume_text = re.sub('RT|cc', ' ', resume_text)
    resume_text = re.sub('#\S+', '', resume_text)
    resume_text = re.sub('@\S+', '  ', resume_text)
    resume_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', resume_text)
    resume_text = re.sub(r'[^\x00-\x7f]', r' ', resume_text)
    resume_text = re.sub('\s+', ' ', resume_text)
    return resume_text.lower()

def train_and_save_model(csv_path):
    # Load data
    df = pd.read_csv(csv_path)
    df['Cleaned_Resume'] = df['Resume'].apply(clean_resume)
    
    # Vectorization
    tfidf = TfidfVectorizer(stop_words='english')
    X = tfidf.fit_transform(df['Cleaned_Resume'])
    y = df['Category']
    
    # Train
    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(X, y)
    
    # Save artifacts
    joblib.dump(tfidf, 'tfidf_vectorizer.pkl')
    joblib.dump(clf, 'resume_model.pkl')
    print("Model and Vectorizer saved successfully.")

def predict_resume(text):
    # Load saved artifacts
    tfidf = joblib.load('tfidf_vectorizer.pkl')
    clf = joblib.load('resume_model.pkl')
    
    cleaned_text = clean_resume(text)
    vectorized_text = tfidf.transform([cleaned_text])
    return clf.predict(vectorized_text)[0]

if __name__ == "__main__":
    # Train the model if artifacts don't exist
    train_and_save_model('resume_dataset.csv')
    
    # Example Usage
    new_resume = "Experienced in Java, Spring Boot, and microservices architecture."
    category = predict_resume(new_resume)
    print(f"The predicted category for the resume is: {category}")


"""
Steps to execute:
1. Install dependencies: Ensure you have scikit-learn, pandas, and joblib installed (pip install scikit-learn pandas joblib).
2. Run the script: python resume_screening.py
3. Output: The script will automatically create tfidf_vectorizer.pkl and resume_model.pkl in your directory, allowing you to run predictions without retraining every time.
"""