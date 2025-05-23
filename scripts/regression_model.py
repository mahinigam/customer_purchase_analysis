import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import logging
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Ensure output directory exists
os.makedirs("plots", exist_ok=True)
os.makedirs("data", exist_ok=True)

ENGINEERED_DATA_PATH = "data/engineered_data.csv"
REGRESSION_RESULTS_PATH = "data/regression_data.csv"

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

# Regression pipeline
def run_regression(df):
    target = 'Total Spend'
    drop_cols = ['Customer ID', 'Purchase Date', 'Gender', 'Payment Method', 'Shipping Type', 'Product Type', 'Add-ons Purchased', 'Loyalty Member', 'SKU', 'Order Status', 'Purchase Weekday']
    X = df.drop(columns=[target] + drop_cols, errors='ignore')
    y = df[target]

    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Models
    models = {
        'Linear Regression': LinearRegression(),
        'Random Forest': RandomForestRegressor(random_state=42),
        'Gradient Boosting': GradientBoostingRegressor(random_state=42)
    }

    results_dict = {}
    for name, model in models.items():
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        results_dict[name] = {
            'MAE': mean_absolute_error(y_test, y_pred),
            'RMSE': np.sqrt(mean_squared_error(y_test, y_pred)),
            'R2': r2_score(y_test, y_pred),
            'Predictions': y_pred,
            'Model': model
        }
        logging.info(f"{name} - R2: {results_dict[name]['R2']:.4f}")

    # GridSearchCV for Random Forest
    logging.info("Running GridSearchCV for Random Forest...")
    rf_params = {
        'n_estimators': [100, 200],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5]
    }
    rf_grid = GridSearchCV(RandomForestRegressor(random_state=42), rf_params, cv=5, scoring='r2', n_jobs=-1, verbose=1)
    rf_grid.fit(X_train_scaled, y_train)
    best_rf = rf_grid.best_estimator_
    y_pred_rf = best_rf.predict(X_test_scaled)
    results_dict['Tuned Random Forest'] = {
        'MAE': mean_absolute_error(y_test, y_pred_rf),
        'RMSE': np.sqrt(mean_squared_error(y_test, y_pred_rf)),
        'R2': r2_score(y_test, y_pred_rf),
        'Predictions': y_pred_rf,
        'Model': best_rf
    }
    logging.info(f"Best Tuned Random Forest Params: {rf_grid.best_params_}")

    # GridSearchCV for Gradient Boosting
    logging.info("Running GridSearchCV for Gradient Boosting...")
    gb_params = {
        'n_estimators': [100, 150],
        'learning_rate': [0.05, 0.1],
        'max_depth': [3, 5]
    }
    gb_grid = GridSearchCV(GradientBoostingRegressor(random_state=42), gb_params, cv=5, scoring='r2', n_jobs=-1, verbose=1)
    gb_grid.fit(X_train_scaled, y_train)
    best_gb = gb_grid.best_estimator_
    y_pred_gb = best_gb.predict(X_test_scaled)
    results_dict['Tuned Gradient Boosting'] = {
        'MAE': mean_absolute_error(y_test, y_pred_gb),
        'RMSE': np.sqrt(mean_squared_error(y_test, y_pred_gb)),
        'R2': r2_score(y_test, y_pred_gb),
        'Predictions': y_pred_gb,
        'Model': best_gb
    }
    logging.info(f"Best Tuned Gradient Boosting Params: {gb_grid.best_params_}")

    # Best model
    best_model_name = max(results_dict.items(), key=lambda x: x[1]['R2'])[0]
    best_predictions = results_dict[best_model_name]['Predictions']
    final_results = pd.DataFrame({
        'Actual': y_test,
        'Predicted': best_predictions
    })
    final_results.to_csv(REGRESSION_RESULTS_PATH, index=False)
    logging.info(f"Best model '{best_model_name}' results saved to {REGRESSION_RESULTS_PATH}")

    # Plot feature importance
    def plot_feature_importance(model, model_name):
        if hasattr(model, 'feature_importances_'):
            importance = model.feature_importances_
            indices = np.argsort(importance)[::-1]
            feature_names = X.columns
            plt.figure(figsize=(10, 6))
            plt.title(f"{model_name} - Feature Importance")
            sns.barplot(x=importance[indices], y=feature_names[indices])
            plt.tight_layout()
            plot_path = f"plots/{model_name.replace(' ', '_').lower()}_feature_importance.png"
            plt.savefig(plot_path)
            plt.close()
            logging.info(f"Saved feature importance plot: {plot_path}")

    plot_feature_importance(best_rf, 'Tuned Random Forest')
    plot_feature_importance(best_gb, 'Tuned Gradient Boosting')

def main():
    df = load_data(ENGINEERED_DATA_PATH)
    if df is not None:
        run_regression(df)
        logging.info("Regression modeling completed successfully.")
    else:
        logging.error("Failed to load data. Exiting.")

if __name__ == "__main__":
    main()
