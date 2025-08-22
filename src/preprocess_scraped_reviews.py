import pandas as pd

# load the raw review data
df = pd.read_csv("data/raw/raw_bank_apps_reviews.csv")

# Clean data
# drop rows with duplicate values
df.drop_duplicates(subset=['review'], inplace=True)

# drop rows with missing values
df.dropna(subset=['review', 'rating', 'date',], inplace=True)

# Format date
# normalize the date column
df['date'] = pd.to_datetime(df['date']).dt.date

# Save cleaned data
df.to_csv("data/processed/processed_banks_app_reviews.csv", index=False)
print("Cleaned data saved to data/processed/processed_banks_app_reviews.csv")



