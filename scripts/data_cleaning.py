import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('C:\\Users\\mahin\\CustomerPurchaseAnalysis\\customer_purchase_analysis\\data\\customer_data.csv')

# Handle missing values
df.dropna(inplace=True)

# Convert purchase_amount to numeric
df['purchase_amount'] = pd.to_numeric(df['purchase_amount'], errors='coerce')

# Example of using the purchase_amount column
df['purchase_amount_log'] = df['purchase_amount'].apply(lambda x: np.log(x + 1))

# Sort by amount
df = df.sort_values('purchase_amount', ascending=False)

# Save cleaned data
df.to_csv('C:\\Users\\mahin\\CustomerPurchaseAnalysis\\customer_purchase_analysis\\data\\customer_data_clean.csv', index=False)
print("Data cleaning complete. Cleaned file saved.")
