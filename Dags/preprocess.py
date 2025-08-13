import datetime
import os
import json
# -*- coding: utf-8 -*-
import sys
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_dir))

current_date = datetime.datetime.now().strftime("%Y-%m-%d")
current_time = datetime.datetime.now().strftime("%H-%M-%S")

def preprocess_data(input_file, output_file):
    """
    Preprocess the data by removing duplicates and null values.
    
    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the preprocessed CSV file.
    """
    # Read the data
    df = pd.read_csv(input_file)
    
    # Ensure the 'lastupdatedate' column is in datetime format
    if 'lastupdatedate' in df.columns:
        df['lastupdatedate'] = pd.to_datetime(df['lastupdatedate'], errors='coerce')
    else:
        raise ValueError("The input file must contain a 'lastupdatedate' column.")
    
    for column in df.columns:
        if df[column].dtype == 'object':
            # Convert string columns to lowercase
            df[column] = df[column].str.lower()
    
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    
    # Remove rows with null values
    df.dropna(inplace=True)
    
    # Save the preprocessed data
    df.to_csv(output_file, index=False)


def main():
    input_file = os.path.join(current_dir, 'data', 'input_data.csv')
    output_file = os.path.join(current_dir, 'data', f'preprocessed_data_{current_date}_{current_time}.csv')
    
    preprocess_data(input_file, output_file)
    print(f"Preprocessed data saved to {output_file}")
if __name__ == "__main__":
    main()