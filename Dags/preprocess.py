import datetime
import os
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
    
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    
    # Remove rows with null values
    df.dropna(inplace=True)
    
    # Save the preprocessed data
    df.to_csv(output_file, index=False)
