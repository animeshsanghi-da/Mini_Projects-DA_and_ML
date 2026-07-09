import pandas as pd

def clean_blinkit_data(input_file, output_file):
    # Load the dataset
    df = pd.read_csv(input_file)
    
    # 1. Convert Order_Date to datetime objects
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    
    # 2. Check for missing values (Basic Audit)
    print("Missing values before cleaning:\n", df.isnull().sum())
    
    # 3. Create a 'Revenue' column (Price * Quantity) for better reporting
    df['Revenue'] = df['Price'] * df['Quantity']
    
    # 4. Save cleaned data
    df.to_csv(output_file, index=False)
    print(f"\nSuccessfully saved cleaned data to {output_file}")
    print(df.head())

if __name__ == "__main__":
    clean_blinkit_data('blinkit_data.csv', 'blinkit_data_cleaned.csv')

"""
Steps to follow:
1. Run the Script: python data_cleaning.py
2. Verification: A new file named blinkit_data_cleaned.csv will be created. This is the file you should import into Power BI Desktop to start building your visualizations.
"""