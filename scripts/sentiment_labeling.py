import pandas as pd

# Load cleaned reviews
df = pd.read_csv("bank_reviews_cleaned.csv")

# Define sentiment labeling function
def label_sentiment(rating):
    if rating <= 2:
        return 'negative'
    elif rating == 3:
        return 'neutral'
    else:
        return 'positive'

# Apply sentiment labeling
df['sentiment'] = df['rating'].apply(label_sentiment)

# Save labeled dataset
df.to_csv("bank_reviews_labeled.csv", index=False)

print("✅ Sentiment labeling complete. Saved as 'bank_reviews_labeled.csv'.")
