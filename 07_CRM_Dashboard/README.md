# CRM Dashboard Project

## Overview
This repository contains the source data and processing scripts for the CRM Dashboard. The project is designed to ingest raw customer relationship management data, clean it for inconsistencies, and prepare it for integration into business intelligence tools like Microsoft Excel or Power BI.

## Project Structure

The project directory contains the following files:

* **`crm_data.csv`**: The primary raw dataset containing customer information (IDs, names, dates, region, and deal values).
* **`crm_dashboard.xlsx`**: An Excel workbook template for final reporting and visualization.
* **`data_cleaning.py`**: A Python automation script that processes the raw CSV file to ensure data integrity and feature engineering.
* **`README.md`**: This documentation file.

## Prerequisites

To run the data cleaning script, you must have Python installed. You will also need the `pandas` library.

You can install the dependency using pip:

```bash
pip install pandas
```

## Usage

Follow these steps to process the CRM data:

1.  **Ensure your raw data is ready**: Make sure `crm_data.csv` is in the same directory as the script.
2.  **Execute the cleaning script**:
    
```bash
python data_cleaning.py
```

3.  **Result**: The script will generate a new file named `cleaned_crm_data.csv`. This file includes a `days_since_last_contact` column, which is useful for identifying churn risks and stale accounts.

## Data Dictionary

| Column | Description |
| :--- | :--- |
| `customer_id` | Unique identifier for each customer. |
| `status` | Current status (Active, Churned, Pending). |
| `days_since_last_contact` | Calculated field: Days elapsed since the last interaction. |
| `deal_value` | The monetary value of the customer deal. |

## Next Steps
Once the `cleaned_crm_data.csv` is generated, you can import this file into your `crm_dashboard.xlsx` or Power BI Desktop to create your visuals, such as:
* **Churn Rate Analysis**: By filtering based on the `status` column.
* **Revenue by Region**: Visualizing `annual_revenue` across North, South, East, and West.
* **Stale Account Alerts**: Using the `days_since_last_contact` field.

## Author
**Animesh Sanghi** | *Google Certified Data Analyst*  
[LinkedIn](https://www.linkedin.com/in/animeshsanghi-da/) | [GitHub](https://github.com/animeshsanghi-da)  
Email: animeshsanghi.da@gmail.com

## License

This project is open-source and free to use.