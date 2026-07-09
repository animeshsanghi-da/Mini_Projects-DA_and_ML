# 30 Programs in KNN: Hyperparameter & Optimization Benchmark

This repository features an exhaustive benchmarking study of the **K-Nearest Neighbors (KNN)** algorithm. It explores how model accuracy and behavior shift across multiple hyperparameter choices, distance metrics, feature scaling methods, and dimensionality reduction strategies using Scikit-Learn's **Iris**, **Wine**, and **Breast Cancer** datasets.

---

## 🚀 Project Architecture

The project is structured into three phases spanning 7 distinct experimental categories:

### **Part 1: Leakage-Free Pipeline Design**
- High-integrity helper function ensuring data transformation fitments (Scaling, PCA) are applied *strictly* post-split (`train_test_split`) to eliminate test-set data leakage.

### **Part 2: The 30 Core Multi-Config Experiments**
- **Category A (Programs 1-10):** Varying K-values (1 through 10) on the Iris dataset to evaluate variance/bias trade-offs.
- **Category B (Programs 11-15):** Testing alternative distance metrics: Euclidean (p=2), Manhattan (p=1), Chebyshev, Minkowski (p=3), and Cosine distance on the Wine dataset.
- **Category C (Programs 16-20):** Evaluation of preprocessing impacts using `StandardScaler`, `MinMaxScaler`, and `RobustScaler` on the Breast Cancer dataset.
- **Category D (Programs 21-25):** Distance-weighted voting vs. uniform voting metrics across varying K-environments.
- **Category E (Programs 26-30):** Dimensionality reduction performance using Principal Component Analysis (PCA) to project higher-dimensional spaces into 2D components.

### **Part 3: Advanced Validation & Mathematical Landscapes**
- **Category F (Robust Validation):** A production-grade **5-Fold Cross-Validation** routine structured safely via a Scikit-Learn `Pipeline` to confirm model stability across folds.
- **Category G (Decision Boundary Visualization):** A visual breakdown detailing spatial territories under K=1 (Overfitting/High Variance) vs. K=9 (Generalized/Smooth Boundary). Optimized with dynamic step-size grids to remain perfectly memory-safe.

---

## 🛠️ Core Engineering Highlights

1. **Data Leakage Mitigation:** Scalers and estimators fit parameters solely from the training folds. Cross-validation applies individual standardizations within localized folds dynamically via Scikit-Learn Pipelines.
2. **Memory-Optimized Meshgrids:** Avoids standard fixed-step space allocations that cause gigabyte-scale memory exhaustion crashes on unscaled data ranges. Instead, it utilizes localized coordinate ranges controlled via `np.linspace`.

---

## 💻 How To Run

1. Make sure your environment has the required libraries installed:
```bash
pip install numpy pandas matplotlib scikit-learn
```

2. Open your preferred environment (Jupyter Notebook, VS Code, Google Colab) and run the cells in `knn_master.ipynb` sequentially.

---

## 👤 Author
**Animesh Sanghi** | *Google Certified Data Analyst*  
🔹 [LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/)  
🔹 [GitHub](https://github.com/animeshsanghi-da)  
✉️ Email: animeshsanghi.da@gmail.com

---

## 📄 License
This project is open-source and free to use.