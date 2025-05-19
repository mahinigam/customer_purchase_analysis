# Customer Purchase Analysis

## **Objective**
This project aims to analyze customer purchase data to derive insights, perform predictive modeling, and visualize trends. The workflow includes data ingestion, cleaning, exploratory data analysis (EDA), regression modeling, and exporting aggregated data for visualization.

---

## **Project Structure**
```
customer_purchase_analysis/
│
├── data/
│   ├── customer_data.csv              # Raw customer data
│   ├── customer_data_clean.csv        # Cleaned customer data
│   ├── regression_results.csv         # Regression model results
│   └── aggregated_data.xlsx           # Aggregated data for visualization
│
├── notebooks/
│   ├── data_ingestion.ipynb           # Load data into MySQL database
│   ├── data_cleaning.ipynb            # Clean and preprocess data
|   ├── feature_engineering.ipynb      # Perform feature engineering on the data
│   ├── eda_analysis.ipynb             # Perform exploratory data analysis
│   ├── regression_model.ipynb         # Train regression model
│   └── visualization_export.ipynb     # Aggregate and export data
│
├── scripts/
|   ├── data_ingestion.py              # Loading into MYSQL databse
|   ├── data_cleaning.py               # Cleaning and preprocessing
|   ├── feature_engineering.py         # Perform feature engineering
│   ├── eda_analysis.py                # EDA functions
│   ├── regression_model.py            # Regression model training
|   ├── visualization_export.py        # Aggregation and exporting data
│
└── README.md                          # Project documentation
```

---

## **Workflow**

### 1. **Data Ingestion**
- **Notebook**: `notebooks/data_ingestion.ipynb`
- **Objective**: Load raw customer data from a CSV file into a MySQL database.
- **Output**: Data stored in the `customer_purchases` table.

### 2. **Data Cleaning**
- **Notebook**: `notebooks/data_cleaning.ipynb`
- **Objective**: Clean and preprocess the raw data.
  - Handle missing values in critical columns.
  - Replace invalid categorical values (e.g., Gender, Loyalty Member, Order Status) with the mode.
  - Convert data types for numeric columns.
  - Fill missing 'Add-ons Purchased' with 'No Add-ons'.
- **Output**: `data/customer_data_clean.csv`

### 3. **Feature Engineering**
- **Notebook**: `notebooks/feature_engineering.ipynb`
- **Objective**: Create new features to enhance analysis.
  - Calculate spend per unit and total spend.
  - Encode categorical variables (Gender, Payment Method, Shipping Type, Product Type).
  - Extract date features (month, day, weekday) from purchase date.
  - Identify loyalty status and add-on usage.
  - Count add-ons and compute add-on cost per unit.
- **Output**: `data/engineered_data.csv`

### 4. **Exploratory Data Analysis (EDA)**
- **Notebook**: `notebooks/eda_analysis.ipynb`
- **Objective**: Analyze trends and visualize data.
  - Purchase amount distribution.
  - Revenue by loyalty status.
  - Time-based sales trends.
  - Identify missing values and dataset overview.
- **Output**: Visualizations and insights.

### 5. **Regression Modeling**
- **Notebook**: `notebooks/regression_model.ipynb`
- **Objective**: Train a linear regression model to predict customer purchase behavior.
- **Output**: `data/regression_results.csv`

### 6. **Data Aggregation & Export**
- **Notebook**: `notebooks/visualization_export.ipynb`
- **Objective**: Aggregate data by region, product category, and purchase frequency, and export results for visualization.
- **Output**: `data/aggregated_data.xlsx`

---

## **Setup Instructions**

### Prerequisites
- Python 3.8+
- MySQL database
- Required Python libraries (see `requirements.txt`)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/mahinigam/customer_purchase_analysis
   cd customer_purchase_analysis
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure MySQL database:
   - Update database credentials in `notebooks/data_ingestion.ipynb`.

4. Run the workflow:
   - Execute notebooks in the following order:
     1. `data_ingestion.ipynb`
     2. `data_cleaning.ipynb`
     3. `eda_analysis.ipynb`
     4. `regression_model.ipynb`
     5. `visualization_export.ipynb`

---

## **Key Features**
- **Data Cleaning**: Ensures high-quality data for analysis by handling missing values, correcting invalid entries, and standardizing data types.
- **Feature Engineering**: Creates new features such as spend per unit, total spend, encoded categorical variables, date-based features, add-on usage, and more to enrich the dataset for analysis and modeling.
- **EDA**: Provides insights into customer behavior, spending patterns, loyalty, and sales trends through visualizations and descriptive statistics.
- **Predictive Modeling**: Uses regression to predict purchase amounts and uncover key drivers of customer spending.
- **Visualization Export**: Aggregates and exports data for business intelligence and visualization tools.

---

## **Next Steps**
- Use the exported data for Tableau or other visualization tools.
- Extend the regression model with additional features or algorithms.
- Explore clustering or segmentation for customer profiling.

---

## **Contact**
For questions or feedback, please contact Mahi Nigam at mahinigam.000@gmail.com.
