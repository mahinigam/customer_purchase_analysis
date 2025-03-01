import pandas as pd
import numpy as np
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

RAW_DATA_PATH = "data/customer_data.csv"
CLEANED_DATA_PATH = "data/customer_data_clean.csv"

def load_data(file_path):
    """Load dataset with error handling."""
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        return None
    
    try:
        df = pd.read_csv(file_path)
        logging.info("Data successfully loaded.")
        return df
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return None

def clean_missing_values(df):
    """Remove rows with missing values."""
    if df is None:
        logging.error("No data available for cleaning.")
        return
    
    try:
        df.dropna(inplace=True)
        logging.info(f"Missing values removed. Rows before: {len(df)}, After: {len(df)}")
        return df
    except Exception as e:
        logging.error(f"Error cleaning missing values: {e}")
        return None

def convert_data_types(df):
    """Convert purchase_amount to numeric."""
    if df is None:
        logging.error("No data available for conversion.")
        return
    
    try:
        df['purchase_amount'] = pd.to_numeric(df['purchase_amount'], errors='coerce')
        logging.info("Data types converted successfully.")
        return df
    except Exception as e:
        logging.error(f"Error converting data types: {e}")
        return None

def feature_engineering(df):
    """Creates log-transformed purchase_amount column."""
    df['purchase_amount_log'] = df['purchase_amount'].apply(lambda x: np.log(x + 1))
    return df

def save_cleaned_data(df, file_path):
    """Saves the cleaned dataset to a CSV file."""
    df = df.sort_values('purchase_amount', ascending=False)
    df.to_csv(file_path, index=False)
    logging.info("Cleaned data saved successfully.")

df = load_data(RAW_DATA_PATH)
if df is not None:
    df = clean_missing_values(df)
    df = convert_data_types(df)
    df = feature_engineering(df)
    save_cleaned_data(df, CLEANED_DATA_PATH)