import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import os

def load_and_split_features_labels(cleaned_data_path='data/processed/job_applicants_cleaned.csv',
                                    online_learning_data_path='data/processed/job_applicants_online_learning_cleaned.csv'):
    df = pd.read_csv(cleaned_data_path)

    # If online learning data exists, merge it
    if os.path.exists(online_learning_data_path):
        df_online = pd.read_csv(online_learning_data_path)
        df = pd.concat([df, df_online], ignore_index=True)
        print(f"✅ Merged online learning data: {len(df_online)} new rows")

    # Features and Target
    X = df.drop(columns=['Employed'])
    y = df['Employed']

    return X, y

def split_train_test(X, y, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    return X_train, X_test, y_train, y_test

def scale_numerical_features(X_train, X_test, numeric_cols):
    scaler = StandardScaler()
    X_train[numeric_cols] = scaler.fit_transform(X_train[numeric_cols])
    X_test[numeric_cols] = scaler.transform(X_test[numeric_cols])
    return X_train, X_test

def select_important_features(X_train, y_train, threshold=0.01):
    print("✅ Running Random Forest feature selection...")

    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)

    importances = pd.Series(rf.feature_importances_, index=X_train.columns)
    selected_features = importances[importances > threshold].index.tolist()

    print(f"✅ Selected {len(selected_features)} features after threshold {threshold}")

    X_train_reduced = X_train[selected_features]
    return X_train_reduced, selected_features


if __name__ == "__main__":
    X, y = load_and_split_features_labels()
    print(f"✅ Loaded X shape: {X.shape}")
    print(f"✅ Loaded y shape: {y.shape}")

    X_train, X_test, y_train, y_test = split_train_test(X, y)
    print(f"✅ Split: X_train: {X_train.shape}, X_test: {X_test.shape}")

    # Identify numeric columns to scale
    numeric_cols = [col for col in X_train.columns if X_train[col].dtype in ['float64', 'int64']]
    print(f"✅ Numeric columns to scale: {numeric_cols}")

    # Scale
    X_train, X_test = scale_numerical_features(X_train, X_test, numeric_cols)

    print("✅ Feature engineering completed")
