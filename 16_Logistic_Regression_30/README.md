# 16_Logistic_Regression_30

This project demonstrates a programmatic approach to Machine Learning by automating exactly **30 variations** of **Logistic Regression** models. Instead of manually writing code for every configuration, this project utilizes controlled nested loops to test various hyperparameters and preprocessing techniques evenly across three distinct datasets (10 experiments per dataset).

## Project Overview
This repository contains a Jupyter Notebook (`logistic_regression_master.ipynb`) that acts as a testing framework. It evaluates the performance of the Logistic Regression algorithm by iterating through different:
* **Datasets:** Iris, Wine, and Breast Cancer (Balanced 10/10/10 split).
* **Preprocessing:** Evaluating the critical impact of feature scaling (`StandardScaler` vs. Raw Data).
* **Hyperparameters:** Variations in optimization `solver` ('lbfgs', 'liblinear') and regularization strengths (`C` values: 0.1, 1.0, 10.0).

## Technologies Used
* **Python**
* **Scikit-Learn** (for dataset loading, pipeline modeling, and evaluation)
* **Pandas/NumPy** (for structured data logging and manipulation)
* **Matplotlib/Seaborn** (for automated comparative visualization)

## How It Works
The script executes a programmatic grid loop to create a comprehensive evaluation architecture, utilizing conditional breaks to guarantee a perfectly balanced experiment distribution.

``` python
# Logic Flow
for dataset in datasets:
    dataset_count = 0
    for scale in [True, False]:
        for solver in ['lbfgs', 'liblinear']:
            for c in [0.1, 1.0, 10.0]:
                if dataset_count >= 10:
                    break
                # Train, Predict, and Log results
                dataset_count += 1
```

## Key Insights & Features
* **Perfect Balance:** Evaluates exactly 10 configurations per dataset to ensure a fair diagnostic baseline.
* **Visual Performance Mapping:** Generates a clean, color-coded Seaborn bar chart indexing all 30 individual runs for instantaneous visual analysis.
* **Automated Optimization Tracking:** Features a dedicated post-loop analysis step that aggregates the results dataframe (`df_results`) to isolate and output the definitive "Best Performing Configuration" for each specific data type.

## How to Run
1. Ensure you have the necessary libraries installed:
``` bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

2. Open `logistic_regression_master.ipynb` in Jupyter Notebook, JupyterLab, or VS Code.
3. Run all cells sequentially to suppress warnings, execute the 30 benchmark experiments, render the performance chart, and print the optimal hyperparameter summary.

## Author
**Animesh Sanghi** | *Google Certified Data Analyst*  
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com

## License
This project is open-source and free to use.