import pandas as pd
from sqlalchemy import create_engine, text
import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define file path
CSV_PATH = 'data/customer_data.csv'

# Read credentials from environment variables
USERNAME = os.getenv('MYSQL_USERNAME')
PASSWORD = os.getenv('MYSQL_PASSWORD')
HOST = os.getenv('MYSQL_HOST')
DATABASE = os.getenv('MYSQL_DATABASE')

def connect_to_db():
    try:
        # Create a new database if it doesn't exist
        engine =  create_engine(f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}')
        connection = engine.conenct()
        connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {DATABASE}"))

        # Connect to the database
        db_engine = create_engine(f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}')

        logging.info("MySQL database connected successfully.")
        return db_engine
    
    except Exception as e:
        logging.error(f"Error connecting to MySQL database: {e}")
        return None

def load_csv_to_mysql(CSV_PATH):
    if not os.path.exists(CSV_PATH):
        logging.error(f"File not found: {CSV_PATH}")
        return None
    
    try:
        df = pd.read_csv(CSV_PATH)
        logging.info("Data loaded successfully from {CSV_PATH}")
    except Exception as e:
        logging.error(f"Error loading data from {CSV_PATH}: {e}")
        return None 

    # Connect to MySQL database
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
