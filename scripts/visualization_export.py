import os
import logging
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Ensure output directory exists
os.makedirs("plots", exist_ok=True)

data_path = "data/cleaned_customer_data.csv"

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

def plot_distribution(df):
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Purchase_Amount'], bins=30, kde=True)
    plt.title('Distribution of Purchase Amount')
    plt.xlabel('Purchase Amount')
    plt.ylabel('Frequency')
    plt.tight_layout()
    path = "plots/purchase_amount_distribution.png"
    plt.savefig(path)
    plt.close()
    logging.info(f"Saved plot: {path}")

def plot_by_gender(df):
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='Gender', y='Purchase_Amount', data=df)
    plt.title('Purchase Amount by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Purchase Amount')
    plt.tight_layout()
    path = "plots/purchase_by_gender.png"
    plt.savefig(path)
    plt.close()
    logging.info(f"Saved plot: {path}")

def plot_by_age_group(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Age_Group', y='Purchase_Amount', data=df, estimator=pd.Series.mean, ci=None)
    plt.title('Average Purchase Amount by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Average Purchase Amount')
    plt.tight_layout()
    path = "plots/avg_purchase_by_age.png"
    plt.savefig(path)
    plt.close()
    logging.info(f"Saved plot: {path}")

def plot_correlation_heatmap(df):
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    path = "plots/correlation_heatmap.png"
    plt.savefig(path)
    plt.close()
    logging.info(f"Saved plot: {path}")

def main():
    df = load_data(data_path)
    if df is not None:
        plot_distribution(df)
        plot_by_gender(df)
        plot_by_age_group(df)
        plot_correlation_heatmap(df)
        logging.info("All visualizations created successfully.")
    else:
        logging.error("Data loading failed. Visualization skipped.")

if __name__ == "__main__":
    main()
