import pandas as pd
import os

def prepare_career_data(raw_path='data/raw/career_recommender.csv',
                        save_path='data/processed/career_recommender_cleaned.csv'):
    # Load the raw data
    df = pd.read_csv(raw_path)

    # Clean up column names
    df.columns = [col.strip() for col in df.columns]

    # Assign the real target column
    TARGET_COLUMN = 'If yes, then what is/was your first Job title in your current field of work? If not applicable, write NA.'

    # Drop rows where label is missing
    df = df.dropna(subset=[TARGET_COLUMN])

    # Rename target column to clean 'Career'
    df = df.rename(columns={TARGET_COLUMN: 'Career'})

    # Fill missing feature columns with 'Unknown'
    feature_cols = [
        'What are your interests?',
        'What are your skills ? (Select multiple if necessary)',
        'What was your course in UG?',
        'What is your UG specialization? Major Subject (Eg; Mathematics)',
    ]

    for col in feature_cols:
        if col in df.columns:
            df[col] = df[col].fillna('Unknown')

    # Save cleaned dataset
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)

    print(f"✅ Data preparation complete. Final dataset shape: {df.shape}")

if __name__ == "__main__":
    prepare_career_data()
