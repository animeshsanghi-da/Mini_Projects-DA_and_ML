# SVM Master: 30 Comparative Experiments

This project provides a comprehensive benchmarking suite for **Support Vector Machines (SVM)**. The notebook `svm_master.ipynb` systematically prepares data and evaluates SVM performance across four classic datasets using a variety of kernel functions and hyperparameter configurations.

## Overview
The goal of this project is to understand how different SVM hyperparameters—specifically **Kernel**, **C (Regularization)**, **Gamma**, and **Degree**—affect classification accuracy across datasets of varying dimensionality and complexity. 

The pipeline includes an optimized preprocessing workflow that utilizes feature standardization to ensure distance-based kernels operate effectively.

## Key Features & Optimizations
* **Automated Feature Scaling:** Uses `StandardScaler` to normalize features upfront, preventing high-magnitude features from dominating the geometric distance calculations.
* **Efficient Memory Management:** Datasets are loaded, split, and scaled exactly once rather than re-calculating for every single experiment.
* **Dynamic Results Tracking:** Results are compiled dynamically into a Pandas DataFrame for easy sorting, filtering, and cross-comparison.

## Datasets Used
The experiments utilize the following standard Scikit-Learn datasets:
* **Iris:** 4 features, 3 classes (Small scale).
* **Wine:** 13 features, 3 classes (Medium scale).
* **Breast Cancer:** 30 features, 2 classes (High-dimensional/Binary).
* **Digits:** 64 features, 10 classes (Image classification).

## Experiment Structure
The experiments are categorized into four parts:

| Dataset | Experiment IDs | Focus |
| :--- | :--- | :--- |
| **Iris** | 1-8 | Kernel comparison & regularization impact |
| **Wine** | 9-16 | Sensitivity to C and Kernel variations |
| **Breast Cancer** | 17-23 | Handling high-dimensional feature spaces |
| **Digits** | 24-30 | Parameter tuning for image data |

## Prerequisites
To run this notebook, ensure you have Python 3.x installed along with the necessary scientific computing libraries. You can install the dependencies via pip:

```bash
pip install pandas scikit-learn
```

## How to Run
1. Clone this repository or download the `svm_master.ipynb` file.
2. Open the file in your preferred Jupyter environment (Jupyter Lab, Jupyter Notebook, or VS Code).
3. Run all cells sequentially.
4. The final cell will compile all results and generate a sorted **Master Leaderboard** DataFrame highlighting the top-performing configurations.

## Key Hyperparameters Explained
* **Kernel:** Specifies the kernel type to be used in the algorithm (`linear`, `poly`, `rbf`, `sigmoid`).
* **C:** Regularization parameter. A smaller C makes the decision surface smoother, while a larger C aims to classify all training examples correctly (at the risk of overfitting).
* **Gamma:** Defines how far the influence of a single training example reaches. Used by 'rbf', 'poly', and 'sigmoid' kernels.
* **Degree:** The degree of the polynomial kernel function (only for 'poly').

## Contributing
Feel free to fork this project and add more experiments, such as including hyperparameter tuning via `GridSearchCV` or `RandomizedSearchCV` to automatically find the optimal parameters for these datasets.

## Author
**Animesh Sanghi** | *Google Certified Data Analyst*  
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com

## License
This project is open-source and free to use.