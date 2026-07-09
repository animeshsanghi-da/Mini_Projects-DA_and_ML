import pandas as pd
import datetime as dt

def clean_crm_data(input_file, output_file):
    # Load the data
    df = pd.read_csv(input_file)

    # 1. Convert date columns to datetime objects
    df['signup_date'] = pd.to_datetime(df['signup_date'])
    df['last_contact_date'] = pd.to_datetime(df['last_contact_date'])

    # 2. Feature Engineering: Calculate days since last contact
    # This helps in identifying stale accounts
    current_date = pd.to_datetime('2026-06-26') # Using current project date
    df['days_since_last_contact'] = (current_date - df['last_contact_date']).dt.days

    # 3. Data Integrity: Ensure no negative deal values
    df['deal_value'] = df['deal_value'].clip(lower=0)

    # 4. Handle Missing Values (Example: If status was missing, mark as 'Unknown')
    df['status'] = df['status'].fillna('Unknown')

    # 5. Save the cleaned dataset
    df.to_csv(output_file, index=False)
    print(f"Data cleaning complete! Cleaned file saved to: {output_file}")
    print(df.head())

if __name__ == "__main__":
    clean_crm_data('crm_data.csv', 'cleaned_crm_data.csv')

"""
Steps to execute this script:
1. Run: python data_cleaning.py
2. Result: This will generate a new file named cleaned_crm_data.csv. Use this cleaned file as the primary data source for your crm_dashboard.xlsx or any Power BI dashboard you create to ensure your visualizations are based on high-quality, processed data.
"""