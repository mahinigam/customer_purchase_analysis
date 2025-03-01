import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define file paths
CLEANED_DATA_PATH = 'data/customer_data_clean.csv'

def load_data(file_path):
    """Load dataset and handle potential errors."""
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

def data_overview(df):
    """Displays dataset structure, summary, and missing values."""
    logging.info("Displaying dataset overview.")
    print("\n--- Data Info ---")
    print(df.info())
    print("\n--- Data Description ---")
    print(df.describe())
    print("\n--- Missing Values ---")
    print(df.isnull().sum())

def plot_purchase_distribution(df):
    """Plots histogram and boxplot for both raw and log-transformed purchase amounts."""
    logging.info("Plotting purchase amount distribution.")

    fig, axes = plt.subplots(2, 1, figsize=(10, 8))
    
    # Histogram of raw purchase amounts
    sns.histplot(df['purchase_amount'], bins=30, kde=True, ax=axes[0])
    axes[0].set_title("Raw Purchase Amount Distribution")
    
    # Boxplot of raw purchase amounts
    sns.boxplot(x=df['purchase_amount'], ax=axes[1])
    axes[1].set_title("Boxplot of Raw Purchase Amount")

    plt.tight_layout()
    plt.show()
    
def plot_log_purchase_distribution(df):
    # Histogram of log-transformed purchase amounts
    logging.info("Plotting log-transformed purchase amount distribution.")

    if 'purchase_amount' not in df:
        logging.error("purchase_amount column not found.")
        return

    df['purchase_amount_log'] = np.log1p(df['purchase_amount']) 
    
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))

    # Histogram of log-transformed purchase amounts
    sns.histplot(df['purchase_amount_log'], bins=30, kde=True, ax=axes[0])
    axes[0].set_title("Log-Transformed Purchase Amount Distribution")
    
    # Boxplot of log-transformed purchase amounts
    sns.boxplot(x=df['purchase_amount_log'], ax=axes[1])
    axes[1].set_title("Boxplot of Log-Transformed Purchase Amount")
    
    plt.tight_layout()
    plt.show()

def plot_spending_by_region(df):
    """Plots average customer spending by region."""
    logging.info("Plotting average spending by region.")
    plt.figure(figsize=(10, 8))
    sns.barplot(x='region', y='purchase_amount', data=df, estimator=np.mean, errorbar=None, palette='viridis', hue='region', legend=False)
    plt.xticks(rotation=45)
    plt.title("Average Customer Spending by Region")
    plt.show()

def plot_purchase_frequency(df):
    """Plots purchase frequency distribution."""
    logging.info("Plotting purchase frequency distribution.")
    plt.figure(figsize=(10, 8))
    sns.countplot(x='purchase_frequency', data=df, palette='coolwarm', hue='purchase_frequency', legend=False)
    plt.xticks(rotation=45)
    plt.title("Purchase Frequency Distribution")
    plt.show()

def perform_eda(df):
    """Executes all EDA functions."""
    if df is None:
        logging.error("No data to analyze.")
        return
    
    try:
        data_overview(df)
        plot_purchase_distribution(df)
        plot_log_purchase_distribution(df)
        plot_spending_by_region(df)
        plot_purchase_frequency(df)
        logging.info("EDA completed successfully.")
    except Exception as e:
        logging.error(f"Error during EDA: {e}")

if __name__ == "__main__":
    df = load_data(CLEANED_DATA_PATH)
    perform_eda(df)
