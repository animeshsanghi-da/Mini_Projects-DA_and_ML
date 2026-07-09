import pandas as pd

def clean_zomato_data(input_file, output_file):
    # Load the dataset
    df = pd.read_csv(input_file)

    # 1. Convert order_date to datetime objects
    df['order_date'] = pd.to_datetime(df['order_date'])

    # 2. Check for missing values (if any) and fill/drop
    # In this dataset, we'll ensure no nulls exist in critical columns
    df.dropna(subset=['order_id', 'restaurant_name', 'order_amount'], inplace=True)

    # 3. Feature Engineering: Create a 'delivery_efficiency' column
    # This helps in visualizing which city/restaurant has faster delivery
    def get_speed(min):
        if min < 30: return 'Fast'
        elif min < 45: return 'Medium'
        else: return 'Slow'

    df['delivery_speed'] = df['delivery_time_min'].apply(get_speed)

    # 4. Sort by date for chronological trend analysis
    df.sort_values(by='order_date', inplace=True)

    # 5. Save the cleaned data
    df.to_csv(output_file, index=False)
    print(f"Data successfully cleaned and saved to {output_file}")
    print(df.head())

if __name__ == "__main__":
    clean_zomato_data('zomato_data.csv', 'cleaned_zomato_data.csv')

"""
Steps to run this:
1. Run the script: python data_cleaning.py
2. Verification: A new file named cleaned_zomato_data.csv will be generated in the same folder. Use this file for your Power BI dashboard import to ensure clean data processing.
"""