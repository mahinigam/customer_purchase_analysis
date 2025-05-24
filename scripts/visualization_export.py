import pandas as pd
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Ensure output directory exists
os.makedirs("plots", exist_ok=True)

ENGINEERED_DATA_PATH = "data/engineered_data.csv"
AGGREGATED_DATA_PATH = "data/aggregated_data.xlsx"

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

def aggregate_data(df):
    agg_data = {}
    logging.info("Starting data aggregation...")

    # Revenue by Product Type
    if 'Product Type' in df.columns:
        agg_data['Revenue_by_Product_Type'] = df.groupby('Product Type')['Total Spend'].sum().reset_index()

    # Revenue by Loyalty
    if 'Loyalty Member' in df.columns:
        agg_data['Revenue_by_Loyalty'] = df.groupby('Loyalty Member')['Total Spend'].sum().reset_index()

    # Monthly Sales
    if 'Purchase Month' in df.columns and 'Purchase Date' in df.columns:
        # Ensure Purchase Date is datetime
        df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])
        monthly_sales = (df.groupby(['Purchase Month', 'Purchase Date'])['Total Spend'].sum().reset_index())

        # Add Month Name column
        monthly_sales['Month Name'] = monthly_sales['Purchase Date'].dt.strftime('%B')

        # Sort by month and date
        monthly_sales = monthly_sales.sort_values(['Purchase Month', 'Purchase Date'])
        agg_data['Monthly_Sales'] = monthly_sales

    # Weekly Sales
    if 'Purchase Weekday' in df.columns and 'Purchase Date' in df.columns:
        weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        weekly_sales = (df.groupby(['Purchase Weekday', 'Purchase Date'])['Total Spend'].sum().reset_index())

        # Ensure weekday order for display
        weekly_sales['Purchase Weekday'] = pd.Categorical(weekly_sales['Purchase Weekday'], categories=weekday_order, ordered=True)

        weekly_sales = weekly_sales.sort_values(['Purchase Weekday', 'Purchase Date'])
        agg_data['Weekly_Sales'] = weekly_sales

    # Age Group Revenue
    if 'Age' in df.columns:
        bins = [18, 25, 35, 45, 55, 65, 100]
        labels = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
        df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)
        agg_data['Revenue_by_Age_Group'] = df.groupby('Age Group')['Total Spend'].sum().reset_index()

    # Gender-wise Revenue
    if 'Gender' in df.columns:
        agg_data['Revenue_by_Gender'] = df.groupby('Gender')['Total Spend'].sum().reset_index()

    # Shipping Preferences
    if 'Shipping Type' in df.columns:
        agg_data['Shipping_Preferences'] = df['Shipping Type'].value_counts().reset_index()
        agg_data['Shipping_Preferences'].columns = ['Shipping Type', 'Count']

    # Add-ons Purchased Frequency
    if 'Add-ons Purchased' in df.columns:
        addons_counts = df['Add-ons Purchased'].value_counts().reset_index()
        addons_counts.columns = ['Add-ons Purchased', 'Count']
        agg_data['Addons_Purchased_Frequency'] = addons_counts

    # Add-ons Count Distribution
    if 'Add-ons Count' in df.columns:
        addon_count_dist = df['Add-ons Count'].value_counts().sort_index().reset_index()
        addon_count_dist.columns = ['Add-ons Count', 'Frequency']
        agg_data['Addons_Count_Distribution'] = addon_count_dist

    logging.info("Aggregated data calculated.")
    return agg_data

def save_to_excel(agg_data, file_path):
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        for sheet_name, data in agg_data.items():
            data.to_excel(writer, sheet_name=sheet_name, index=False)
            logging.info(f"Saved {sheet_name} to {file_path}")
    logging.info("All sheets saved successfully.")

def main():
    df = load_data(ENGINEERED_DATA_PATH)
    if df is not None:
        agg_data = aggregate_data(df)
        save_to_excel(agg_data, AGGREGATED_DATA_PATH)
        logging.info("All visualizations created successfully.")
    else:
        logging.error("Data loading failed. Visualization skipped.")
        logging.error("Data loading failed. Visualization skipped.")

if __name__ == "__main__":
    main()
