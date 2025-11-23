import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import warnings
warnings.filterwarnings('ignore')

def load_and_explore_data(filepath):
    """
    Load and explore the movie rating dataset
    """
    print("Loading movie dataset...")
    df = pd.read_csv(filepath, encoding='latin-1')
    
    print("\nDataset Info:")
    print(df.info())
    print("\nFirst few rows:")
    print(df.head())
    print("\nDataset shape:", df.shape)
    print("\nMissing values:")
    print(df.isnull().sum())
    
    return df

def preprocess_data(df):
    """
    Preprocess movie rating data
    """
    data = df.copy()
    
    # Fill missing values
    for col in data.columns:
        if data[col].dtype == 'object':
            data[col].fillna(data[col].mode()[0] if not data[col].mode().empty else 'Unknown', inplace=True)
        else:
            data[col].fillna(data[col].median(), inplace=True)
    
    # Encode categorical variables
    label_encoders = {}
    categorical_cols = data.select_dtypes(include=['object']).columns
    
    for col in categorical_cols:
        if col != 'Rating':
            le = LabelEncoder()
            data[col] = le.fit_transform(data[col].astype(str))
            label_encoders[col] = le
    
    print("\nPreprocessed data shape:", data.shape)
    print("\nFeature columns:", data.columns.tolist())
    
    return data, label_encoders

def train_and_evaluate_model(X_train, X_test, y_train, y_test):
    """
    Train and evaluate movie rating prediction model
    """
    print("\n" + "="*60)
    print("Training Models...".center(60))
    print("="*60)
    
    # Linear Regression
    print("\n1. Linear Regression")
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    lr_pred = lr_model.predict(X_test)
    
    lr_mse = mean_squared_error(y_test, lr_pred)
    lr_rmse = np.sqrt(lr_mse)
    lr_mae = mean_absolute_error(y_test, lr_pred)
    lr_r2 = r2_score(y_test, lr_pred)
    
    print(f"   RMSE: {lr_rmse:.4f}")
    print(f"   MAE: {lr_mae:.4f}")
    print(f"   R² Score: {lr_r2:.4f}")
    
    # Random Forest Regressor
    print("\n2. Random Forest Regressor")
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=10)
    rf_model.fit(X_train, y_train)
    rf_pred = rf_model.predict(X_test)
    
    rf_mse = mean_squared_error(y_test, rf_pred)
    rf_rmse = np.sqrt(rf_mse)
    rf_mae = mean_absolute_error(y_test, rf_pred)
    rf_r2 = r2_score(y_test, rf_pred)
    
    print(f"   RMSE: {rf_rmse:.4f}")
    print(f"   MAE: {rf_mae:.4f}")
    print(f"   R² Score: {rf_r2:.4f}")
    
    # Feature importance for Random Forest
    if hasattr(rf_model, 'feature_importances_'):
        feature_importance = pd.DataFrame({
            'feature': X_train.columns,
            'importance': rf_model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        print("\nTop 10 Important Features:")
        print(feature_importance.head(10))
    
    # Choose best model
    best_model = rf_model if rf_r2 > lr_r2 else lr_model
    best_model_name = "Random Forest" if rf_r2 > lr_r2 else "Linear Regression"
    best_rmse = rf_rmse if rf_r2 > lr_r2 else lr_rmse
    best_r2 = rf_r2 if rf_r2 > lr_r2 else lr_r2
    
    print("\n" + "="*60)
    print(f"Best Model: {best_model_name}")
    print(f"RMSE: {best_rmse:.4f}")
    print(f"R² Score: {best_r2:.4f}")
    print("="*60)
    
    return best_model, best_model_name, best_r2

def main():
    """
    Main function for movie rating prediction
    """
    print("="*60)
    print("Movie Rating Prediction".center(60))
    print("="*60)
    
    # Note: Use movie rating dataset
    # Example: IMDb dataset or similar
    filepath = 'movies.csv'  # Update this path
    
    try:
        # Load and explore data
        df = load_and_explore_data(filepath)
        
        # Assume the dataset has a 'Rating' column as target
        if 'Rating' not in df.columns:
            print("\nError: 'Rating' column not found in dataset!")
            print("Available columns:", df.columns.tolist())
            return
        
        # Preprocess data
        data, label_encoders = preprocess_data(df)
        
        # Split features and target
        X = data.drop('Rating', axis=1)
        y = data['Rating']
        
        # Split into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        print(f"\nTraining set size: {len(X_train)}")
        print(f"Testing set size: {len(X_test)}")
        
        # Train and evaluate models
        model, model_name, r2 = train_and_evaluate_model(X_train, X_test, y_train, y_test)
        
        print("\n" + "="*60)
        print("Model training completed successfully!")
        print("="*60)
        
    except FileNotFoundError:
        print(f"\nError: Dataset file '{filepath}' not found!")
        print("\nPlease provide a movie rating dataset with the following columns:")
        print("- Rating (target variable)")
        print("- Genre, Director, Actors, etc. (features)")
        print("\nYou can use datasets from:")
        print("- https://www.kaggle.com/datasets")
        print("- IMDb datasets")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main()
