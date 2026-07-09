import pandas as pd

def clean_habit_data(input_file, output_file):
    # 1. Load the data
    df = pd.read_csv(input_file)
    
    # 2. Convert Date to datetime format
    df['Date'] = pd.to_datetime(df['Date'])
    
    # 3. Fill missing numeric values with the median of their columns
    # This prevents errors during analysis due to empty cells
    numeric_cols = ['Duration_Minutes', 'Mood_Score']
    for col in numeric_cols:
        df[col] = df[col].fillna(df[col].median())
    
    # 4. Fill missing categorical values
    df['Energy_Level'] = df['Energy_Level'].fillna('Medium')
    df['Notes'] = df['Notes'].fillna('No notes')
    
    # 5. Ensure Status is consistent
    df['Status'] = df['Status'].str.strip().str.capitalize()
    
    # 6. Save the cleaned data for your dashboard
    df.to_csv(output_file, index=False)
    print(f"Data cleaned successfully! Saved to {output_file}")
    
    # Display summary to verify
    print("\n--- Data Summary ---")
    print(df.info())

if __name__ == "__main__":
    clean_habit_data('habit_data.csv', 'cleaned_habit_data.csv')

"""
Steps to follow:
1. Run the script: python data_cleaning.py
2. Result: This will generate a new file called cleaned_habit_data.csv which is ready for you to import into Excel or any visualization tool for your portfolio dashboard.
"""