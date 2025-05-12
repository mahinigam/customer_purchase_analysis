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
│   ├── eda_analysis.ipynb             # Perform exploratory data analysis
│   ├── regression_model.ipynb         # Train regression model
│   └── visualization_export.ipynb     # Aggregate and export data
│
├── scripts/
|   ├── data_ingestion.py              # Loading into MYSQL databse
|   ├── data_cleaning.py               # Cleaning and preprocessing
│   ├── eda_analysis.py                # EDA functions
│   ├── regression_model.py            # Regression model training
|   ├── visualization_export.py        # Aggregation and exporting data
│
└── README.md                          # Project documentation
```

---

## **Workflow**

### 1️⃣ **Data Ingestion**
- **Notebook**: `notebooks/data_ingestion.ipynb`
- **Objective**: Load raw customer data from a CSV file into a MySQL database.
- **Output**: Data stored in the `customer_purchases` table.

### 2️⃣ **Data Cleaning**
- **Notebook**: `notebooks/data_cleaning.ipynb`
- **Objective**: Clean and preprocess the raw data.
  - Handle missing values.
  - Convert data types.
  - Add log-transformed features.
- **Output**: `data/customer_data_clean.csv`

### 3️⃣ **Exploratory Data Analysis (EDA)**
- **Notebook**: `notebooks/eda_analysis.ipynb`
- **Objective**: Analyze trends and visualize data.
  - Purchase amount distribution.
  - Spending by region.
  - Purchase frequency.
- **Output**: Visualizations and insights.

### 4️⃣ **Regression Modeling**
- **Notebook**: `notebooks/regression_model.ipynb`
- **Objective**: Train a linear regression model to predict customer purchase behavior.
- **Output**: `data/regression_results.csv`

### 5️⃣ **Data Aggregation & Export**
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
- **Data Cleaning**: Ensures high-quality data for analysis.
- **EDA**: Provides insights into customer behavior.
- **Predictive Modeling**: Uses regression to predict purchase amounts.
- **Visualization Export**: Aggregates data for business insights.

---

## **Next Steps**
- Use the exported data for Tableau or other visualization tools.
- Extend the regression model with additional features or algorithms.
- Explore clustering or segmentation for customer profiling.

---

## **Contact**
For questions or feedback, please contact Mahi Nigam at mahinigam.000@gmail.com.
