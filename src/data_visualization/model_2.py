# src/data_visualization/model_2.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os

# Load processed dataset
df = pd.read_csv('data/processed/job_applicants_cleaned.csv')

# ----- 1. Correlation heatmap (without Country columns) -----
features_for_corr = df.drop(columns=[col for col in df.columns if col.startswith('Country_')])

corr = features_for_corr.corr()

plt.figure(figsize=(12, 10))
sns.heatmap(corr, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap (excluding Country columns)')
plt.tight_layout()
os.makedirs('plots', exist_ok=True)
plt.savefig('plots/correlation_heatmap.png')
plt.close()
print("✅ Saved: correlation_heatmap.png")

# ----- 2. Top correlated features with 'Employed' -----
correlations_with_employed = corr['Employed'].drop('Employed').sort_values(ascending=False)

plt.figure(figsize=(8, 6))
sns.barplot(x=correlations_with_employed.values, y=correlations_with_employed.index)
plt.title('Top Feature Correlations with Being Employed')
plt.xlabel('Correlation Coefficient')
plt.ylabel('Feature')
plt.tight_layout()
plt.savefig('plots/top_employment_correlations.png')
plt.close()
print("✅ Saved: top_employment_correlations.png")

# ----- 3. Loss curve if available -----
try:
    history = joblib.load('models/training_history.pkl')

    plt.figure(figsize=(8, 6))
    plt.plot(history['loss'], label='Training Loss')
    plt.plot(history['val_loss'], label='Validation Loss')
    plt.title('Training vs Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.tight_layout()
    plt.savefig('plots/loss_curve.png')
    plt.close()
    print("✅ Saved: loss_curve.png")

except FileNotFoundError as e:
    print(f"⚠️ Warning: Could not load training history. {e}")
