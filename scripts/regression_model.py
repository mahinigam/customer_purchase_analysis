import pandas as pd
import logging
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define file path
DATA_PATH = 'C:\\Users\\mahin\\CustomerPurchaseAnalysis\\customer_purchase_analysis\\data\\customer_data_clean.csv'
RESULTS_PATH = 'C:\\Users\\mahin\\CustomerPurchaseAnalysis\\customer_purchase_analysis\\data\\regression_results.csv'

def load_data(file_path):
    """Load dataset safely."""
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        return None
    try:
        df = pd.read_csv(file_path)
        logging.info("Data loaded successfully.")
        return df
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return None

def train_regression(df):
    """Train a linear regression model."""
    if df is None:
        logging.error("No data available for training.")
        return
    
    try:
        # Creating a feature for transaction order
        df['transaction_id'] = range(1, len(df) + 1)
        X = df[['transaction_id']]
        y = df['purchase_amount_log']

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Make predictions
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        logging.info(f"Model trained successfully. Mean Squared Error: {mse}")

        # Save results
        results = pd.DataFrame({'Actual': y_test, 'Predicted': predictions})
        results.to_csv(RESULTS_PATH, index=False)
        logging.info(f"Regression results saved: {RESULTS_PATH}")

    except Exception as e:
        logging.error(f"Error during model training: {e}")

if __name__ == "__main__":
    df = load_data(DATA_PATH)
    train_regression(df)
