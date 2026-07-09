# 20_Electricity_Consumption_Prediction

This project focuses on predicting daily electricity consumption (in kWh) based on environmental and temporal factors. By leveraging weather data and time-based features, the model provides robust forecasts of grid demand while strictly adhering to time-series machine learning best practices.

## Project Overview

The core objective is to build an end-to-end machine learning pipeline that takes environmental input (Temperature, Humidity) and temporal metadata (Day of the Week, Is_Holiday) to forecast electricity usage. Unlike standard tabular regression, this pipeline implements strict chronological validation to replicate real-world deployment scenarios.

### Pipeline Stages & Key Features
* **Exploratory Data Analysis (EDA):** Visualizes the non-linear relationship between temperature and energy consumption, alongside weekly consumption distributions using `seaborn` and `matplotlib`.
* **Data Preprocessing & Hygiene:** Handles datetime conversion, chronological sequence sorting, and cleans the feature space by removing zero-variance variables (such as redundant `Year` columns).
* **Time-Series Validation Strategy:** Implements a chronological index-based split (80% train / 20% test) instead of a random shuffle. This completely eliminates **data leakage**, ensuring the model evaluates solely on its ability to predict the future given past patterns.
* **Model Training:** Utilizes a **Random Forest Regressor** capable of mapping complex interactions between heatwaves, weekends, and load spikes.
* **Evaluation & Visual Share:** Tracks performance via the $R^2$ metric and generates an evaluation timeline plot comparing actual vs. predicted consumption trends.
* **Model Serialization:** Exports the trained model to a production-ready `.pkl` file using `joblib`.

## Directory Structure

``` text
20_Electricity_Consumption_Prediction/
├── electricity_data.csv        # Historical tabular dataset (July - Sept 2026)
├── electricity_pipeline.ipynb  # Comprehensive Jupyter Notebook (EDA, Split, Train, Evaluation)
├── model.pkl                   # Serialized production Random Forest model
└── README.md                   # Project documentation
```

## Prerequisites

Ensure you have Python installed, then install the necessary data science dependencies:

``` bash
pip install pandas scikit-learn joblib matplotlib seaborn
```

## How to Run

1. **Open the Notebook:** Launch Jupyter Notebook or JupyterLab in your local repository environment.
   ``` bash
   jupyter notebook
   ```
2. **Execute the Pipeline:** Open `electricity_pipeline.ipynb` and execute the cells sequentially from top to bottom.
3. **Verification:** * Observe the initial correlation boxplots during the EDA phase.
   * Review the final trend visualization chart matching actual values against model predictions.
   * Confirm that a freshly generated `model.pkl` file has appeared in your root project directory.

## Model Performance & Methodology

By treating this dataset as a strict chronological sequence, the model avoids overfitting and delivers high generalizability:
* **Algorithm:** `RandomForestRegressor`
* **Validation Split:** Chronological boundary split (No random shuffling)
* **Target Metric ($R^2$ Score):** ~0.8407 
  *(Note: While a random shuffle yields an artificially inflated $R^2$ of ~0.94 due to temporal data leakage, our realistic timeline split achieves an honest, robust ~0.84—proving genuine predictive performance on unseen future intervals).*

## Author
**Animesh Sanghi** | *Google Certified Data Analyst*  
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com

## License
This project is open-source and free to use.