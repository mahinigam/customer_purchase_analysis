import pandas as pd
from sqlalchemy import create_engine

# MySQL connection details (Update with your credentials)
USERNAME = 'root'
PASSWORD = 'root'
HOST = 'localhost'
DATABASE = 'customer_analysis'

# Establish connection to MySQL
engine = create_engine(f'mysql+mysqlconnector://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}')

# Load CSV data
csv_file = 'data/customer_data.csv'
df = pd.read_csv(csv_file)

# Load into MySQL
table_name = 'customer_purchases'
df.to_sql(table_name, engine, if_exists='replace', index=False)
print(f"Data successfully loaded into MySQL table: {table_name}")
