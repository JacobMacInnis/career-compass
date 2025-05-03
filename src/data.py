import pandas as pd

# df = pd.read_csv('data/processed/job_applicants_cleaned.csv')

# print(df['Employed'].value_counts())

df = pd.read_csv('data/processed/job_applicants_cleaned.csv')

correlations = df.corr()['Employed'].sort_values(ascending=False)

print(correlations)