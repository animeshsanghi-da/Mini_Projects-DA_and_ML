# Restaurant Sales Exploratory Data Analysis

## Project Overview
This repository contains an Exploratory Data Analysis (EDA) of restaurant sales transactions. By processing raw order data, this project aims to uncover patterns in customer behavior, identify top-performing menu items, and optimize operational strategies.

## Methodology
The analysis follows the Google Data Analytics framework:
* **Ask**: Define the business objective (analyzing revenue and operational efficiency).
* **Prepare**: Load and verify the `restaurant_sales.csv` dataset.
* **Process**: Clean the data, format timestamps, and prepare for analysis.
* **Analyze & Share**: Create visualizations to identify trends in categories, volume, payments, peak hours, and customer sentiment.
* **Act**: Formulate actionable business recommendations.

## Dataset Structure
The dataset (`restaurant_sales.csv`) contains:
- **Transaction Details**: `Order_ID`, `Date`, `Time`, `Table_No`
- **Product Details**: `Item_Name`, `Category`, `Price`, `Quantity`, `Total_Sales`
- **Customer Metrics**: `Payment_Method`, `Customer_Rating`

## Key Business Insights & Recommendations
Based on the comprehensive analysis performed in `sales_eda.ipynb`:
1. **Operational Efficiency**: Data indicates distinct peak hours for lunch and dinner. Management should optimize staff scheduling to ensure maximum service quality during these high-traffic windows.
2. **Quality Control**: Sentiment analysis revealed variations in ratings across categories. We recommend a "Quality Improvement Initiative" for lower-rated items while aggressively promoting high-rated favorites.
3. **Menu Optimization**: 'Main Course' is the primary revenue driver. We should increase average check size by designing cross-selling bundles (e.g., pairing Mains with Starters or Beverages).
4. **Inventory Management**: Top-selling items require precise inventory tracking. Implementing a Just-In-Time (JIT) stock management system for these high-volume ingredients will minimize wastage and prevent stockouts.
5. **Payment Infrastructure**: High reliance on UPI and Credit Cards necessitates robust digital payment systems to ensure a smooth, frictionless customer checkout experience.

## Data Limitations
* **Sample Size**: The analysis is based on a limited dataset, which may not capture long-term seasonal trends (e.g., holidays).
* **Missing Context**: We lack demographic information (e.g., age, loyalty status), limiting the ability to perform hyper-targeted marketing.
* **Subjectivity**: 'Customer_Rating' is subjective and may be influenced by external factors outside the restaurant's control.

## Prerequisites
To run the analysis locally, ensure you have the following libraries installed:

```bash
pip install pandas matplotlib seaborn
```

## How to Explore
1. Clone this repository.
2. Ensure `restaurant_sales.csv` is in the same directory as the notebook.
3. Open `sales_eda.ipynb` using Jupyter Notebook, JupyterLab, or VS Code.
4. Run the cells sequentially to view the analysis and visualizations.

## Author
**Animesh Sanghi** | *Google Certified Data Analyst*  
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com

## License
This project is open-source and free to use.