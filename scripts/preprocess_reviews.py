# scripts/preprocess_reviews.py

import pandas as pd

df = pd.read_csv("data/raw_reviews.csv")

# Clean data
df.drop_duplicates(subset=['review'], inplace=True)
df.dropna(subset=['review', 'rating', 'date'], inplace=True)

# Format date
df['date'] = pd.to_datetime(df['date']).dt.date

# Save cleaned data
df.to_csv("data/clean_reviews.csv", index=False)
print("Cleaned data saved to data/clean_reviews.csv")
