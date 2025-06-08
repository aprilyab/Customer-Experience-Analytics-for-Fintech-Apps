import pandas as pd

# Load the CSV file
df = pd.read_csv("bank_reviews.csv")

# Remove duplicates
df.drop_duplicates(inplace=True)

# Drop rows with missing essential columns
df.dropna(subset=['review', 'rating', 'date', 'bank'], inplace=True)

# Normalize date format
# Step 1: Convert to datetime (handle errors as NaT)
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Step 2: Drop invalid dates (NaT)
df = df[df['date'].notna()]

# Step 3: Format dates to YYYY-MM-DD
df['date'] = df['date'].dt.strftime('%Y-%m-%d')

# Add source column
df['source'] = 'google_play'

# Reorder and filter columns
df = df[['review', 'rating', 'date', 'bank', 'source']]

# Save cleaned file
df.to_csv("bank_reviews_cleaned.csv", index=False)

print("✅ Dates normalized. Saved cleaned file as 'bank_reviews_cleaned.csv'.")
