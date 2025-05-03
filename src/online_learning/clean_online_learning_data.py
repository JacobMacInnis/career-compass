import pandas as pd
import os

def clean_online_learning_data(
    input_path='data/raw/job_applicants_online_learning.csv',
    output_path='data/processed/job_applicants_online_learning_cleaned.csv',
    reference_path='data/processed/job_applicants_cleaned.csv'  # <-- NEW
):
    # Load online learning data
    df = pd.read_csv(input_path)

    # Drop non-feature columns
    df = df.drop(columns=['id', 'timestamp'], errors='ignore')

    # Rename any skill columns to match the original cleaned data names
    rename_map = {
        'Skill_HTML_CSS': 'Skill_HTML/CSS',
        'Skill_Node_js': 'Skill_Node.js',
        'Skill_React_js': 'Skill_React.js',
        'Skill_Bash_Shell': 'Skill_Bash/Shell',
        'Skill_CSharp': 'Skill_C#',
        'Skill_Microsoft_SQL_Server': 'Skill_Microsoft SQL Server',
        # Add any others if you have mismatch
    }
    df = df.rename(columns=rename_map)

    # One-hot encode the categorical variables
    categorical_cols = ['Age', 'Accessibility', 'EdLevel', 'Gender', 'MentalHealth', 'MainBranch', 'Country']
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    # 🚨 NEW: Force match columns with reference dataset
    ref = pd.read_csv(reference_path)

    # Add any missing columns in online learning df
    for col in ref.columns:
        if col not in df.columns:
            df[col] = 0

    # Reorder columns to match reference
    df = df[ref.columns]

    # Fill any remaining missing values (just in case)
    df = df.fillna(0)

    # Save cleaned
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned and aligned online learning data saved to {output_path}")

if __name__ == "__main__":
    clean_online_learning_data()
