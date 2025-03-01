import pandas as pd
from sqlalchemy import create_engine
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define file path
CSV_PATH = 'data/customer_data.csv'

# MySQL connection details
USERNAME = 'root'
PASSWORD = 'root'
HOST = 'localhost'
DATABASE = 'customer_analysis'

def connect_to_db():
    """Connect to MySQL database."""
    try:
        engine = create_engine(f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}')
        logging.info("MySQL database connected successfully.")
        return engine
    except Exception as e:
        logging.error(f"Error connecting to MySQL database: {e}")
        return None

def load_csv_to_mysql(CSV_PATH):
    """Load CSV data into MySQL database."""
    if not os.path.exists(CSV_PATH):
        logging.error(f"File not found: {CSV_PATH}")
        return None
    
    try:
        df = pd.read_csv(CSV_PATH)
        logging.info("Data loaded successfully from {CSV_PATH}")
    except Exception as e:
        logging.error(f"Error loading data from {CSV_PATH}: {e}")
        return None 

    # Load into MySQL
    table_name = 'customer_purchases'
    engine = connect_to_db()
    if not engine:
        logging.error("Database connection failed.")
        return None
    
    try:
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        logging.info(f"Data successfully loaded into MySQL table: {table_name}")
    except Exception as e:
        logging.error(f"Error loading data into MySQL: {e}")
    finally:
        engine.dispose()
        logging.info("Database connection closed.")

if __name__ == "__main__":
    load_csv_to_mysql(CSV_PATH)
