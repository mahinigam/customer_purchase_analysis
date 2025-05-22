import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import os

# Ensure plots directory exists
os.makedirs("plots", exist_ok=True)

ENGINEERED_DATA_PATH = "data/engineered_data.csv"

def load_data(file_path):
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        return None
    
    try:
        df = pd.read_csv(file_path)
        logging.info(f"Data successfully loaded from {file_path}")
        return df
    
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        return None
    
# 1. Revenue and Loyalty Analysis
def revenue_loyalty_analysis(df):
    sns.boxplot(data=df, x='Loyalty Member', y='Total Price')
    plt.title("Revenue by Loyalty Status")
    plt.show()
    plt.savefig("plots/revenue_loyalty_analysis.png")
    plt.close()

# 2. Time-based Sales Trends
def time_sales_trends(df):
    # Monthly sales
    monthly_sales = df.groupby('Purchase Month')['Total Price'].sum()
    monthly_sales.plot(kind='bar', title='Monthly Sales')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.show()
    plt.savefig("plots/monthly_sales.png")
    plt.close()

    # Weekly sales
    weekday_sales = df.groupby('Purchase Weekday')['Total Price'].sum().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    weekday_sales.plot(kind='bar', title='Sales by Weekday', color='purple')
    plt.xticks(rotation=45)
    plt.xlabel('Weekday')
    plt.ylabel('Total Sales')
    plt.show()
    plt.savefig("plots/weekday_sales.png")
    plt.close()

# 3. Customer Behaviour Pattern
def customer_behaviour_analysis(df):
    sns.scatterplot(data=df, x='Quantity', y='Spend per Unit', hue='Is Loyal')
    plt.title("Spend per Unit vs Quantity by Loyalty Status")
    plt.show()
    plt.savefig("plots/customer_behaviour_analysis.png")
    plt.close()

# 4. Gender-wise Purchase Behaviour
def gender_purchase_behaviour(df):
    sns.barplot(data=df, x='Gender', y='Total Price', estimator=sum)
    plt.title("Total Revenue by Gender")
    plt.show()
    plt.savefig("plots/gender_purchase_behaviour.png")
    plt.close()

# 5. Payment and Shipping Preferences
def payment_shipping_preferences(df):
    # Payment preferences
    sns.countplot(data=df, x='Payment Method')
    plt.title("Preferred Payment Methods")
    plt.xticks(rotation=45)
    plt.show()
    plt.savefig("plots/payment_preferences.png")
    plt.close()

    # Shipping preferences
    sns.countplot(data=df, x='Shipping Type')
    plt.title("Preferred Shipping Methods")
    plt.xticks(rotation=45)
    plt.show()
    plt.savefig("plots/shipping_preferences.png")
    plt.close()

# 6. Correlation Matrix
def correlation_matrix(df):
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("Correlation Heatmap")
    plt.show()
    plt.savefig("plots/correlation_matrix.png")
    plt.close()

# 7. Product Type Analysis
def product_type_analysis(df):
    sns.countplot(data=df, x='Product Type')
    plt.title("Product Type Distribution")
    plt.xticks(rotation=45)
    plt.show()
    plt.savefig("plots/product_type_analysis.png")
    plt.close()

# 8. Age group Analysis
def age_group_analysis(df):
    age_bins = [18, 25, 35, 45, 55, 65, 100]
    age_labels = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
    df['Age Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)
    sns.barplot(data=df, x='Age Group', y='Total Price', estimator=sum)
    plt.title("Revenue by Age Group")
    plt.show()
    plt.savefig("plots/age_group_analysis.png")
    plt.close()

# 9. Add-ons Analysis
def addons_analysis(df):
    sns.countplot(data=df, x='Add-ons Purchased', order=df['Add-ons Purchased'].value_counts().index)
    plt.title("Frequency of Add-ons Purchased")
    plt.xticks(rotation=45)
    plt.show()
    plt.savefig("plots/addons_analysis.png")
    plt.close()

# 10. Category-wise Spend
def category_spend_analysis(df):
    sns.barplot(data=df, x='Product Type', y='Total Price', estimator=sum)
    plt.title("Total Spend by Product Type")
    plt.xticks(rotation=45)
    plt.show()
    plt.savefig("plots/category_spend_analysis.png")
    plt.close()

# 11. Rating Analysis
def rating_analysis(df):
    sns.histplot(data=df, x='Rating', bins=5, kde=True)
    plt.title("Distribution of Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Frequency")
    plt.show()
    plt.savefig("plots/rating_analysis.png")
    plt.close()

# 12. Pairplot for Feature Relationships
def pairplot(df):
    sns.pairplot(df[['Total Price', 'Spend per Unit', 'Quantity', 'Age']])
    plt.suptitle("Pairplot of Key Features", y=1.02)
    plt.show()
    plt.savefig("plots/pairplot.png")
    plt.close()

def main():
    df = load_data(ENGINEERED_DATA_PATH)
    if df is not None:
        revenue_loyalty_analysis(df)
        time_sales_trends(df)
        customer_behaviour_analysis(df)
        gender_purchase_behaviour(df)
        payment_shipping_preferences(df)
        correlation_matrix(df)
        product_type_analysis(df)
        age_group_analysis(df)
        addons_analysis(df)
        category_spend_analysis(df)
        rating_analysis(df)
        pairplot(df)
        logging.info("All analyses completed successfully.")
    else:
        logging.error("Data loading failed. Exiting analysis.")
    
if __name__ == "__main__":
    main()