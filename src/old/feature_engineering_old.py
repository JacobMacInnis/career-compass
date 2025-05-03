import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

def load_and_split_features_labels(cleaned_data_path='data/processed/career_recommender_cleaned.csv'):
    df = pd.read_csv(cleaned_data_path)

    feature_cols = [
        'What are your interests?',
        'What are your skills ? (Select multiple if necessary)',
        'What was your course in UG?',
        'What is your UG specialization? Major Subject (Eg; Mathematics)',
    ]

    TARGET_COLUMN = 'Career'

    X = df[feature_cols]
    y = df[TARGET_COLUMN]

    return X, y
def filter_rare_classes(X, y, min_samples=2):
    # Filter out classes that have fewer than min_samples examples
    counts = pd.Series(y).value_counts()
    valid_classes = counts[counts >= min_samples].index
    mask = y.isin(valid_classes)
    return X[mask], y[mask]

def encode_features(X):
    # One-hot encode all categorical feature columns
    X_encoded = pd.get_dummies(X)
    return X_encoded

def encode_labels(y):
    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)
    return y_encoded, label_encoder

def split_train_test(X_encoded, y_encoded, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = train_test_split(
        X_encoded, y_encoded,
        test_size=test_size,
        random_state=random_state,
        stratify=y_encoded
    )
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    # Load and split
    X, y = load_and_split_features_labels()

    X, y = filter_rare_classes(X, y, min_samples=2)

    X_encoded = encode_features(X)

    y_encoded, label_encoder = encode_labels(y)

    X_train, X_test, y_train, y_test = split_train_test(X_encoded, y_encoded)

    print(f"✅ Data ready: X_train: {X_train.shape}, X_test: {X_test.shape}")
    print(f"✅ y_train classes: {len(set(y_train))}")
