import os

# Path to your CSV
csv_path = 'data/processed/career_recommender_cleaned.csv'

# Get size in bytes
file_size_bytes = os.path.getsize(csv_path)

# Convert to megabytes
file_size_mb = file_size_bytes / (1024 * 1024)

print(f"File Size: {file_size_mb:.2f} MB")
