# Linear Regression Master Portfolio: A 30-Model Benchmarking Experiment

This repository contains a comprehensive, systematic benchmarking project that builds, tests, and evaluates **30 distinct variations** of Linear Regression models using the classic **California Housing Dataset**. 

Rather than just building a single model, this project serves as an experimental sandbox demonstrating how feature engineering, data preprocessing, complexity scaling, and regularization affect a model's predictive power, stability, and error distribution.

---

## 🗺️ The 30-Model Roadmap

The project is structured into 6 logical experimental phases, tracking a total of 30 model iterations:

| Model Range | Experimental Focus | Key Variants / Hyperparameters | Purpose |
| :--- | :--- | :--- | :--- |
| **Models 1 – 5** | **Feature Subsets** | From a single feature (`MedInc`) up to all 8 features | Analyzes feature importance and predictive baseline. |
| **Models 6 – 10** | **Feature Scaling** | None, Standard, MinMax, Robust Scalers | Evaluates how data centering and scaling impact linear equations. |
| **Models 11 – 15**| **Model Complexity** | Polynomial Degrees (1 to 5) on `MedInc` | Visually tracks the transition from underfitting to severe overfitting. |
| **Models 16 – 20**| **Ridge Regularization (L2)** | Alpha values: `0.1`, `1.0`, `10.0`, `100.0`, `1000.0` | Demonstrates coefficient shrinkage to prevent overfitting. |
| **Models 21 – 25**| **Lasso Regularization (L1)** | Alpha values: `0.001`, `0.01`, `0.1`, `1.0`, `10.0` | Demonstrates automatic feature selection through zeroed weights. |
| **Models 26 – 30**| **Diagnostics & Evaluation**| MSE, RMSE, R² Metrics & Residual Plots | Assesses model health, homoscedasticity, and error distribution. |

---

## 🔬 Core Experimental Phases Explained

### 1. Feature Selection Variations (Models 1–5)
Tests how different combinations of economic, structural, and geographic features impact the **R² score**. It contrasts models using isolated single indicators (like Median Income) against complete multidimensional feature sets.

### 2. Feature Preprocessing & Scaling (Models 6–10)
Examines how normalizing the data scale impacts standard OLS (Ordinary Least Squares) regression. This phase utilizes:
* `StandardScaler`: Centers data to a mean of 0 and standard deviation of 1.
* `MinMaxScaler`: Compresses data features strictly between a 0 and 1 range.
* `RobustScaler`: Scales features using statistics that are robust to outliers (IQR).

### 3. Polynomial Regression & Bias-Variance Tradeoff (Models 11–15)
Introduces non-linear mathematical relationships by expanding a single feature (`MedInc`) up to a 5th-degree polynomial. This highlights the precise inflection point where a model stops learning generalized patterns and begins overfitting to training noise.

### 4. Regularization Techniques (Models 16–25)
Introduces penalties to the loss function to handle multicollinearity and complex feature spaces:
* **Ridge Regression (L2 Penalty):** Forces feature coefficients closer to zero, smoothing out model wildness.
* **Lasso Regression (L1 Penalty):** Drives completely unhelpful feature coefficients directly to zero, acting as an automated embedded feature selection tool.

### 5. Model Health & Residual Diagnostics (Models 26–30)
Evaluates a baseline comprehensive linear model using multiple validation viewpoints:
* **Statistical Metrics:** Comparative evaluation using Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and the Coefficient of Determination (R² Score).
* **Residual Analysis:** A scatter plot of predictions vs. errors to check for homoscedasticity, paired with an error distribution histogram to verify that the errors are normally distributed.

---

## 🚀 How to Run

### Prerequisites
Ensure you have a clean Python environment with the required libraries installed. You can install them via pip:

insert_ticks bash
pip install numpy pandas matplotlib seaborn scikit-learn
insert_ticks

### Execution Steps
1. Clone this repository to your local machine.
2. Open `linear_regression_master.ipynb` in your preferred environment (Jupyter Notebook, JupyterLab, or VS Code).
3. Run the cells sequentially from top to bottom to witness the metrics evolve across all 30 variations.

---

## 📈 Key Project Takeaways
* **More features don't always mean a better model:** Selecting high-correlation inputs yields cleaner results than throwing raw, noisy data at a matrix.
* **The Overfitting Cliff:** Increasing polynomial complexity boosts training performance but will cause test metrics to crater if left unchecked.
* **Regularization is essential:** Tuning hyperparameter math (Alpha) is vital to finding the optimal balance between high bias (underfitting) and high variance (overfitting).

---

## 👤 Author

**Animesh Sanghi** | *Google Certified Data Analyst*  
👉 [LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/)  
👉 [GitHub](https://github.com/animeshsanghi-da)  
📧 Email: animeshsanghi.da@gmail.com

---

## 📄 License

This project is open-source, free to use, and distributed under the MIT License.