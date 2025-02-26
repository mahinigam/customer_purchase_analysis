import pandas as pd
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define file paths
DATA_PATH = 'C:\\Users\\mahin\\CustomerPurchaseAnalysis\\customer_purchase_analysis\\data\\customer_data_clean.csv'
OUTPUT_PATH = 'C:\\Users\\mahin\\CustomerPurchaseAnalysis\\customer_purchase_analysis\\data\\aggregated_data.csv'

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

def aggregate_data(df):
    """Aggregate purchase amount by region, product category, and purchase frequency."""
    if df is None:
        logging.error("No data available for aggregation.")
        return
    
    try:
        # Aggregate total purchase amount by region
        region_sales = df.groupby('region')['purchase_amount'].sum().reset_index()
        region_sales.rename(columns={'purchase_amount': 'total_sales'}, inplace=True)

        # Aggregate total purchase amount by product category
        category_sales = df.groupby('product_category')['purchase_amount'].sum().reset_index()
        category_sales.rename(columns={'purchase_amount': 'total_sales'}, inplace=True)

        # Aggregate total purchase amount by purchase frequency
        frequency_sales = df.groupby('purchase_frequency')['purchase_amount'].sum().reset_index()
        frequency_sales.rename(columns={'purchase_amount': 'total_sales'}, inplace=True)

        # Save all aggregated data into one file
        with pd.ExcelWriter(OUTPUT_PATH.replace('.csv', '.xlsx')) as writer:
            region_sales.to_excel(writer, sheet_name="Region Sales", index=False)
            category_sales.to_excel(writer, sheet_name="Category Sales", index=False)
            frequency_sales.to_excel(writer, sheet_name="Frequency Sales", index=False)

        logging.info(f"Aggregated data exported successfully: {OUTPUT_PATH.replace('.csv', '.xlsx')}")

    except Exception as e:
        logging.error(f"Error during data aggregation: {e}")

if __name__ == "__main__":
    df = load_data(DATA_PATH)
    aggregate_data(df)
