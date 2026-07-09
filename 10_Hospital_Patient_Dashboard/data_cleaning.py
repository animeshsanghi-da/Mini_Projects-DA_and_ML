import pandas as pd
import numpy as np

def clean_hospital_data(input_file, output_file):
    # Load the data
    df = pd.read_csv(input_file)
    
    # 1. Convert Date columns to datetime objects
    df['Admission_Date'] = pd.to_datetime(df['Admission_Date'])
    df['Discharge_Date'] = pd.to_datetime(df['Discharge_Date'])
    
    # 2. Calculate 'Length_of_Stay' (Days)
    df['Length_of_Stay'] = (df['Discharge_Date'] - df['Admission_Date']).dt.days
    
    # 3. Calculate 'Cost_Per_Day'
    df['Cost_Per_Day'] = df['Treatment_Cost'] / df['Length_of_Stay'].replace(0, 1)
    
    # 4. Handle any missing values (example: fill numeric with median, object with mode)
    df.fillna({'Department': 'General'}, inplace=True)
    
    # 5. Extract month/year for easier Power BI time-intelligence
    df['Month'] = df['Admission_Date'].dt.month_name()
    
    # Save the cleaned file
    df.to_csv(output_file, index=False)
    print(f"Data cleaned and saved successfully to {output_file}")
    print(df.head())

if __name__ == "__main__":
    clean_hospital_data('patient_data.csv', 'cleaned_patient_data.csv')

"""
Run the Script to generate cleaned_patient_data.csv.
"""