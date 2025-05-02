import pandas as pd

def explore_data(filepath='data/raw/job_applicants.csv'):
    df = pd.read_csv(filepath)

    print("\n✅ Dataset loaded")
    print(f"Shape: {df.shape}")

    print("\n📚 Columns:")
    print(df.columns.tolist())

    print("\n🔍 Sample Data:")
    print(df.head())

    print("\n🧹 Missing Values:")
    print(df.isnull().sum())

    print("\n📊 Data Types:")
    print(df.dtypes)

# ComputerSkills     0
# Employed           0
# dtype: int64

# 📊 Data Types:
# Unnamed: 0          int64
# Age                object
# Accessibility      object
# EdLevel            object
# Employment          int64
# Gender             object
# MentalHealth       object
# MainBranch         object
# YearsCode           int64
# YearsCodePro        int64
# Country            object
# PreviousSalary    float64
# HaveWorkedWith     object
# ComputerSkills      int64
# Employed            int64
# dtype: object



if __name__ == "__main__":
    explore_data()

