import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_explore_data():
    """
    Load and explore the Iris dataset
    """
    print("="*60)
    print("Iris Flower Classification".center(60))
    print("="*60)
    
    # Load the Iris dataset
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = pd.Series(iris.target, name='species')
    
    print("\nDataset Information:")
    print(f"Number of samples: {len(X)}")
    print(f"Number of features: {X.shape[1]}")
    print(f"\nFeatures: {list(iris.feature_names)}")
    print(f"\nTarget classes: {list(iris.target_names)}")
    
    print("\nFirst few rows:")
    df = pd.concat([X, y], axis=1)
    print(df.head())
    
    print("\nClass distribution:")
    print(y.value_counts().sort_index())
    
    print("\nStatistical summary:")
    print(X.describe())
    
    return X, y, iris.target_names

def train_and_evaluate_models(X_train, X_test, y_train, y_test, target_names):
    """
    Train multiple models and compare their performance
    """
    models = {
        'K-Nearest Neighbors': KNeighborsClassifier(n_neighbors=3),
        'Decision Tree': DecisionTreeClassifier(random_state=42, max_depth=5),
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'Support Vector Machine': SVC(kernel='rbf', random_state=42)
    }
    
    results = {}
    
    print("\n" + "="*60)
    print("Model Training and Evaluation".center(60))
    print("="*60)
    
    for name, model in models.items():
        print(f"\n{name}:")
        print("-" * 40)
        
        # Train the model
        model.fit(X_train, y_train)
        
        # Make predictions
        y_pred = model.predict(X_test)
        
        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)
        
        # Cross-validation score
        cv_scores = cross_val_score(model, X_train, y_train, cv=5)
        
        print(f"Training Accuracy: {model.score(X_train, y_train):.4f}")
        print(f"Testing Accuracy: {accuracy:.4f}")
        print(f"Cross-validation Score: {cv_scores.mean():.4f} (+/- {cv_scores.std():.4f})")
        
        results[name] = {
            'model': model,
            'accuracy': accuracy,
            'predictions': y_pred
        }
    
    # Find best model
    best_model_name = max(results, key=lambda x: results[x]['accuracy'])
    best_model = results[best_model_name]['model']
    best_accuracy = results[best_model_name]['accuracy']
    best_predictions = results[best_model_name]['predictions']
    
    print("\n" + "="*60)
    print(f"Best Model: {best_model_name}")
    print(f"Best Accuracy: {best_accuracy:.4f}")
    print("="*60)
    
    # Detailed classification report for best model
    print("\nClassification Report (Best Model):")
    print(classification_report(y_test, best_predictions, target_names=target_names))
    
    # Confusion matrix
    print("\nConfusion Matrix (Best Model):")
    cm = confusion_matrix(y_test, best_predictions)
    print(cm)
    
    return best_model, best_model_name, best_accuracy

def main():
    """
    Main function for Iris flower classification
    """
    # Load and explore data
    X, y, target_names = load_and_explore_data()
    
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    
    print(f"\nTraining set size: {len(X_train)}")
    print(f"Testing set size: {len(X_test)}")
    
    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Convert back to DataFrame
    X_train_scaled = pd.DataFrame(X_train_scaled, columns=X.columns)
    X_test_scaled = pd.DataFrame(X_test_scaled, columns=X.columns)
    
    # Train and evaluate models
    best_model, best_model_name, best_accuracy = train_and_evaluate_models(
        X_train_scaled, X_test_scaled, y_train, y_test, target_names
    )
    
    # Example prediction
    print("\n" + "="*60)
    print("Example Prediction".center(60))
    print("="*60)
    
    # Use first test sample
    sample = X_test_scaled.iloc[0:1]
    prediction = best_model.predict(sample)
    
    print("\nSample features:")
    print(sample)
    print(f"\nPredicted species: {target_names[prediction[0]]}")
    print(f"Actual species: {target_names[y_test.iloc[0]]}")
    
    print("\n" + "="*60)
    print("Classification completed successfully!".center(60))
    print("="*60)

if __name__ == "__main__":
    main()
