import datetime
import os
import sys
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(current_dir))
# Get the current date and time for file naming
sys.path.append(os.path.dirname(current_dir))

current_date = datetime.datetime.now().strftime("%Y-%m-%d")
current_time = datetime.datetime.now().strftime("%H-%M-%S")
current_date_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def preprocess_data(input_file, output_file):
    """
    Preprocess the data by removing duplicates and null values.
    
    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the preprocessed CSV file.
    """
    # Read the data
    df = pd.read_csv(input_file)
    df = df.dropna(axis=1, how='all')  # Drop columns that are completely null
    
    # Remove duplicates
    df.drop_duplicates(inplace=True)

    df.absorbance = df.absorbance.astype(str)  # Convert absorbance to string if not already
    # Ensure the 'lastupdatedate' column is in datetime format
    
    # Remove rows with null values
    df.dropna(inplace=True)
    
    # Save the preprocessed data
    df.to_csv(output_file, index=False)
def main():
    input_file = os.path.join(current_dir, 'data', 'input_data.csv')
    output_file = os.path.join(current_dir, 'data', f'preprocessed_data_{current_date}_{current_time}.csv')
    
    preprocess_data(input_file, output_file)
    print(f"Preprocessed data saved to {output_file}")

def main():
    input_file = os.path.join(current_dir, 'data', 'input_data.csv')
    output_file = os.path.join(current_dir, 'data', f'preprocessed_data_{current_date}_{current_time}.csv')
    
    preprocess_data(input_file, output_file)
    print(f"Preprocessed data saved to {output_file}")
    
if __name__ == "__main__":
    main()