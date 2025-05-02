import pandas as pd
import os

def prepare_career_data(
    raw_data_path='data/raw/job_applicants.csv',
    processed_data_path='data/processed/job_applicants_cleaned.csv',
    top_skills_count=20
):
    # Load raw data
    df = pd.read_csv(raw_data_path)
    print(f"✅ Loaded dataset with shape: {df.shape}")

    # Drop 'Unnamed: 0' column
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])

    # Fill missing 'HaveWorkedWith' with 'None'
    df['HaveWorkedWith'] = df['HaveWorkedWith'].fillna('None')

    # Split skills into lists
    df['SkillsList'] = df['HaveWorkedWith'].apply(lambda x: x.split(';') if isinstance(x, str) else [])

    # Build a list of top N most common skills
    all_skills = [skill for sublist in df['SkillsList'] for skill in sublist]
    skill_counts = pd.Series(all_skills).value_counts()
    top_skills = skill_counts.head(top_skills_count).index.tolist()
    print(f"✅ Top {top_skills_count} skills selected: {top_skills}")

    # One-hot encode top skills
    for skill in top_skills:
        df[f'Skill_{skill}'] = df['SkillsList'].apply(lambda skills: int(skill in skills))
    for col in ['EdLevel', 'Gender', 'MentalHealth', 'MainBranch', 'Country']:
        print(f"\nUnique values for {col}:")
        print(df[col].unique())

    # Drop Employment column (we don't want to leak employment status into model)
    if 'Employment' in df.columns:
        df = df.drop(columns=['Employment'])

    # Drop raw 'HaveWorkedWith' and 'SkillsList'
    df = df.drop(columns=['HaveWorkedWith', 'SkillsList'])

    # Handle categorical encoding manually for basic fields
    categorical_cols = ['Age', 'Accessibility', 'EdLevel', 'Gender', 'MentalHealth', 'MainBranch', 'Country']
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

    # Handle numeric missing values if any (none expected, but safe)
    df = df.fillna(0)

    # Save cleaned file
    os.makedirs(os.path.dirname(processed_data_path), exist_ok=True)
    df.to_csv(processed_data_path, index=False)
    print(f"✅ Processed data saved to {processed_data_path}")
    print(f"✅ Final shape: {df.shape}")


if __name__ == "__main__":
    prepare_career_data()
