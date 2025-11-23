import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_explore_data(filepath):
    """
    Load and explore the Titanic dataset
    Dataset URL: https://www.kaggle.com/c/titanic/data
    """
    print("Loading Titanic dataset...")
    df = pd.read_csv(filepath)
    
    print("\nDataset Info:")
    print(df.info())
    print("\nFirst few rows:")
    print(df.head())
    print("\nMissing values:")
    print(df.isnull().sum())
    print("\nSurvival rate:")
    print(df['Survived'].value_counts(normalize=True))
    
    return df

def preprocess_data(df):
    """
    Preprocess and clean the Titanic dataset
    """
    # Create a copy to avoid modifying original
    data = df.copy()
    
    # Fill missing values
    data['Age'].fillna(data['Age'].median(), inplace=True)
    data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
    data['Fare'].fillna(data['Fare'].median(), inplace=True)
    
    # Drop columns that won't be used
    data.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
    
    # Convert categorical variables to numerical
    data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
    data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)
    
    print("\nPreprocessed data shape:", data.shape)
    print("\nFeatures:", data.columns.tolist())
    
    return data

def train_model(X_train, X_test, y_train, y_test):
    """
    Train Random Forest model and evaluate performance
    """
    # Initialize and train the model
    print("\nTraining Random Forest Classifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42, max_depth=5)
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate model
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nModel Accuracy: {accuracy:.4f}")
    
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    print("\nConfusion Matrix:")
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    
    # Feature importance
    feature_importance = pd.DataFrame({
        'feature': X_train.columns,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print("\nTop Features:")
    print(feature_importance.head(10))
    
    return model, accuracy

def main():
    """
    Main function to run the Titanic survival prediction
    """
    print("="*60)
    print("Titanic Survival Prediction".center(60))
    print("="*60)
    
    # Note: Download the dataset from Kaggle
    # https://www.kaggle.com/c/titanic/data
    filepath = 'train.csv'  # Update this path
    
    try:
        # Load and explore data
        df = load_and_explore_data(filepath)
        
        # Preprocess data
        data = preprocess_data(df)
        
        # Split features and target
        X = data.drop('Survived', axis=1)
        y = data['Survived']
        
        # Split into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
        
        # Scale features
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        # Convert back to DataFrame for feature names
        X_train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns)
        X_test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns)
        
        # Train and evaluate model
        model, accuracy = train_model(X_train_scaled, X_test_scaled, y_train, y_test)
        
        print("\n" + "="*60)
        print(f"Final Model Accuracy: {accuracy:.2%}")
        print("="*60)
        
    except FileNotFoundError:
        print(f"\nError: Dataset file '{filepath}' not found!")
        print("Please download the Titanic dataset from:")
        print("https://www.kaggle.com/c/titanic/data")
        print("\nPlace the 'train.csv' file in the same directory as this script.")

if __name__ == "__main__":
    main()
