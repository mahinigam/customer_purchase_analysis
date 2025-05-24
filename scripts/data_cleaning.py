import pandas as pd
import numpy as np
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

RAW_DATA_PATH = "data/customer_data.csv"
CLEANED_DATA_PATH = "data/customer_data_clean.csv"

# Create data directory if it doesn't exist
os.makedirs(os.path.dirname(CLEANED_DATA_PATH), exist_ok=True)

def load_data(file_path):
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        return None
    
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Data successfully loaded from {file_path}")
        return df
    
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return None

# Convert data types
def convert_data_types(df):
    if df is None:
        logging.error("No data to convert.")
        return
    
    try:
        columns = ['Customer ID', 'Age', 'Rating', 'Total Price', 'Unit Price', 'Quantity', 'Add-on Total']

        df[columns] = df[columns].apply(pd.to_numeric, errors='coerce')
        logging.info("Data types converted successfully.")
        return df
    
    except Exception as e:
        logging.error(f"Error converting data types: {e}")
        return None
    
# Handle invalid values
def handle_invalid_values(df):
    if df is None:
        logging.error("No data to handle,")
        return
    
    try:
        # Replaces invalid gender entries with the mode
        valid_genders = ['Male', 'Female']
        invalid_genders_mask = ~df['Gender'].isin(valid_genders)
        df.loc[invalid_genders_mask, 'Gender'] = df['Gender'].mode()[0]

        # Replaces invalid loyalty status with the mode
        valid_loyalty_status = ['No', 'Yes']
        invalid_loyaltystatus_mask = ~df['Loyalty Member'].isin(valid_loyalty_status)
        df.loc[invalid_loyaltystatus_mask, 'Loyalty Member'] = df['Loyalty Member'].mode()[0]

        # Replaces invalid order status with the mode
        valid_order_status = ['Cancelled', 'Completed']
        invalid_orderstatus_mask = ~df['Order Status'].isin(valid_order_status)
        df.loc[invalid_orderstatus_mask, 'Order Status'] = df['Order Status'].mode()[0]


        logging.info(f"Invalid genders handled.")
        return df
    
    except Exception as e:
        logging.error(f"Error handling invalid values: {e}")
        return None
    
# Handle missing values
def clean_missing_values(df):
    if df is None:
        logging.error("No data to clean.")
        return
    
    try:
        length_before = len(df)

        # Drop rows with missing values in critical columns
        df.dropna(subset=['Customer ID', 'Age', 'Gender', 'Loyalty Member', 'Product Type', 'SKU', 'Rating', 'Order Status', 'Payment Method', 'Total Price', 'Unit Price', 'Quantity', 'Purchase Date', 'Shipping Type'], inplace=True)

        # Replaces missing values in 'Add-ons Purchased' with 'No Add-ons'
        df['Add-ons Purchased'] = df['Add-ons Purchased'].fillna('No Add-ons')

        length_after = len(df)

        logging.info(f"Missing values handled. Rows before: {length_before}, After: {length_after}")
        return df
    
    except Exception as e:
        logging.error(f"Error cleaning missing values: {e}")
        return None

def handle_outliers(df):
    if df is None:
        logging.error("No data to handle outliers.")
        return
    try:
        numeric_cols = ['Age', 'Total Price', 'Unit Price', 'Quantity', 'Add-on Total']
        for col in numeric_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            before = len(df)
            df = df[(df[col] >= lower) & (df[col] <= upper)]
            after = len(df)
            logging.info(f"Outliers removed in {col}: {before - after}")
        return df
    except Exception as e:
        logging.error(f"Error handling outliers: {e}")
        return df

def transform_skewed_data(df):
    if df is None:
        logging.error("No data to transform.")
        return
    try:
        skewed_cols = ['Total Price', 'Unit Price', 'Add-on Total']
        for col in skewed_cols:
            df[f'log_{col}'] = np.log1p(df[col])
        logging.info("Log transformation applied to skewed columns.")
        return df
    except Exception as e:
        logging.error(f"Error transforming data: {e}")
        return df

def print_summary_statistics(df):
    if df is None:
        logging.error("No data for summary statistics.")
        return
    try:
        stats = df.describe(include='all')
        stats.to_csv("data/summary_statistics.csv")
        logging.info("Summary statistics saved to data/summary_statistics.csv")
        # Also print a concise summary to console
        print(stats)
        # Value counts for key categorical columns
        for col in ['Gender', 'Loyalty Member', 'Order Status', 'Payment Method', 'Product Type']:
            print(f"\nValue counts for {col}:\n{df[col].value_counts()}")
    except Exception as e:
        logging.error(f"Error generating summary statistics: {e}")

# Save cleaned data
def save_cleaned_data(df, file_path):
    if df is None:
        logging.error("No data to save.")
        return
    
    try:
        df.to_csv(file_path, index=False)
        logging.info("Cleaned data saved successfully.")

    except Exception as e:
        logging.error(f"Error saving cleaned data: {e}")

def main():
    df = load_data(RAW_DATA_PATH)
    if df is not None:
        df = convert_data_types(df)
        df = handle_invalid_values(df)
        df = clean_missing_values(df)
        df = handle_outliers(df)
        df = transform_skewed_data(df)
        print_summary_statistics(df)
        save_cleaned_data(df, CLEANED_DATA_PATH)

if __name__ == "__main__":
    main()