import pandas as pd
import numpy as np
import logging
import os

#v Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

CLEANED_DATA_PATH = "../data/customer_data_clean.csv"
ENGINEERED_DATA_PATH = "../data/engineered_data.csv"

# Make sure the data directory exists
os.makedirs(os.path.dirname(ENGINEERED_DATA_PATH), exist_ok=True)

def load_data(file_path):
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        return None
    
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Data loaded successfully from {file_path}")
        return df
    
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return None
    
# Feature Engineering
def feature_engineering(df):
    if df is None:
        logging.error("DataFrame is None, cannot perform feature engineering.")
        return None
    
    try:
        # 1. Spend per Unit
        df['Spend per Unit'] = df['Total Price'] / df['Quantity']

        # 2. Check Customer Loyalty
        df['Is Loyal'] = df['Loyalty Member'].map({'Yes': 1, 'No': 0})

        # 3. Date Features
        df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])
        df['Purchase Month'] = df['Purchase Date'].dt.month
        df['Purchase Day'] = df['Purchase Date'].dt.day
        df['Purchase Weekday'] = df['Purchase Date'].dt.day_name()

        # 4. Check Add-ons
        df['Has Add-ons'] = df['Add-ons Purchased'].apply(lambda x: 0 if x == 'No Add-ons' else 1)

        # 5. Count Add-ons
        df['Add-ons Count'] = df['Add-ons Purchased'].apply(lambda x: len(str(x).split(',')) if x != 'No Add-ons' else 0)

        # 6. Encode Gender
        df['Gender_Encoded'] = df['Gender'].map({'Male': 0, 'Female': 1})

        # 7. Encode Payment Method
        payment_dummies = pd.get_dummies(df['Payment Method'], prefix='Pay').astype(int)
        df = pd.concat([df, payment_dummies], axis=1)

        # 8. Encode Shipping Type
        ship_dummies = pd.get_dummies(df['Shipping Type'], prefix='Ship').astype(int)
        df = pd.concat([df, ship_dummies], axis=1)

        # 9. Encode Product Type
        product_dummies = pd.get_dummies(df['Product Type'], prefix='Product').astype(int)
        df = pd.concat([df, product_dummies], axis=1)

        # 10. Add-ons Cost per Unit
        df['Add-on Cost per Unit'] = df['Add-on Total'] / df['Quantity']

        # 11. Total Spend
        df['Total Spend'] = df['Total Price'] + df['Add-on Total']

        logging.info("Feature engineering completed successfully.")
        return df
    
    except Exception as e:
        logging.error(f"Error during feature engineering: {e}")
        return None
    
# Save the engineered data
def save_feature_engineered_data(df, file_path):
    if df is None:
        logging.error("DataFrame is None, cannot save to CSV.")
        return
    
    try:
        df.to_csv(file_path, index=False)
        logging.info(f"Feature Engineered data saved successfully to {file_path}")

    except Exception as e:
        logging.error(f"Error saving data to CSV: {e}")

def main():
    df = load_data(CLEANED_DATA_PATH)
    if df is not None:
        df = feature_engineering(df)
        save_feature_engineered_data(df, ENGINEERED_DATA_PATH) 

if __name__ == "__main__":
    main()