# Student Placement Prediction System

## Project Overview
This project builds a robust, end-to-end predictive machine learning pipeline to determine if a student will be successfully placed or not based on key academic and professional performance metrics. 

By leveraging a **Random Forest Classifier**, the system models the complex interactions between academic standings (GPA), technical milestones (Projects, Internships), and interpersonal metrics (Soft Skills). To transform this from a basic baseline model into a production-ready repository, the workflow incorporates Exploratory Data Analysis (EDA), Stratified K-Fold Cross-Validation to guarantee model stability against synthetic data splits, Feature Importance explainability, and a live deployment inference module.

## Technology Stack
- **Language**: Python
- **Libraries**: 
  - *Data Manipulation*: Pandas
  - *Machine Learning*: Scikit-learn
  - *Visualization*: Matplotlib, Seaborn
  - *Model Serialization*: Joblib
- **Algorithm**: Random Forest Classifier

## Project Structure
```
19_Student_Placement_Prediction/
├── placement_data.csv         # Tabular dataset tracking student performance metrics
├── placement_pipeline.ipynb   # Complete interactive notebook containing EDA, training, and validation
├── model.pkl                  # Serialized (frozen) Random Forest model binary
└── README.md                  # This documentation file
```

## Workflow Architecture
1. **Data Ingestion & Cleaning**: Loading the tabular student dataset, verifying shape configurations, and screening for missing values or anomalous rows.
2. **Feature Engineering**: Deleting data-leaking operational artifacts like `Student_ID` and mapping the categorical target variable (`Placement_Status`) into a clean binary integer classification target (`Placed`: 1, `Not Placed`: 0).
3. **Exploratory Data Analysis (EDA)**: Utilizing an advanced 2x2 Seaborn dashboard to systematically isolate trends across GPA brackets, internship volumes, and soft skill variances against placement counts.
4. **Model Architecture & Cross-Validation**: Instantiating a Random Forest classifier and validating generalizability using a **Stratified 5-Fold Cross-Validation** routine to combat potential evaluation bias.
5. **Model Evaluation & Explainability**: Evaluating final metrics through standard confusion matrices and classification reports, paired with an extraction of tree-based Feature Importances to explain model decision bounds.
6. **Production Serialization**: Storing the operational pipeline to disk as a `model.pkl` binary file.
7. **Live Pipeline Inference**: Executing an active mock inference script that loads the serialized model to score and calculate raw placement probabilities for an unlabelled, real-time student profile.

## How to Run
1. Ensure your local environment has the full stack of required Python packages installed:
```bash
pip install pandas scikit-learn joblib matplotlib seaborn
```

2. Fire up a local Jupyter notebook server or open the project within an IDE workspace:
```bash
jupyter notebook placement_pipeline.ipynb
```

3. Run the notebook cells sequentially from top to bottom.
4. Upon successful completion, the 2x2 EDA graphs and feature distribution charts will generate inline, validation scores will print out, and a localized `model.pkl` asset will freeze into your active project root folder.

## Core Notebook Enhancements & Key Insights

### 1. Exploratory Data Analysis Dashboard
The notebook renders a modern 2x2 subplot configuration to analyze performance characteristics across placement splits:
- **Distribution of Placement Status**: A baseline balance check of the target classes.
- **GPA Distribution vs Placement Status**: Highlights structural thresholds where higher GPA averages directly correlate with placement likelihood.
- **Number of Internships vs Placement Status**: Visually captures that completed professional internships heavily tilt classification odds toward successful hiring.
- **Soft Skills Score vs Placement Status**: Tracks how interpersonal qualities impact placement thresholds.

### 2. Validation & Synthetic Data Reality Check
While standard train-test splitting yields perfect accuracy due to the highly clean, linear boundaries present in the `placement_data.csv` dataset, relying strictly on a single 80-20 split can introduce sampling bias. 

To demonstrate industry-grade reliability, the updated pipeline runs a **Stratified 5-Fold Cross-Validation**. This partitions the data five separate times while maintaining original class distributions, confirming that the high predictive performance is uniform and robust across all subsets of the data.

### 3. Feature Urgency Profile (Explainability)
Instead of treating the Random Forest as a "black box," the repository charts relative feature importance. This maps exactly which attributes carry the highest predictive weight, helping university administrators or data analysts pinpoint the most critical levers for student success.

### 4. Production-Level Inference Simulation
The pipeline concludes with a fully autonomous inference pipeline snippet. It simulates how an active web API or user interface would process incoming data:
```python
# Simulating a live production API call
loaded_pipeline = joblib.load('model.pkl')
unseen_candidate = pd.DataFrame([{'GPA': 3.3, 'Internships': 1, 'Projects': 2, 'Soft_Skills_Score': 7}])

predicted_class = loaded_pipeline.predict(unseen_candidate)
placement_probability = loaded_pipeline.predict_proba(unseen_candidate)[0][1]
```

## Author
**Animesh Sanghi** | *Google Certified Data Analyst*  
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com

## License
This project is open-source and free to use.