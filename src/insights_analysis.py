import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("data/processed/final_bank_apps_review_data.csv")

# Positive drivers
drivers_keywords = ['fast', 'easy', 'smooth', 'reliable', 'secure', 'userfriendly', 'good', 'excellent']

# Negative pain points
pain_keywords = ['crash', 'slow', 'error', 'problem', 'bug', 'dont', 'doesnt', 'cant', 'worst', 'issue']


drivers_count = {}
pain_count = {}

for bank in df['bank'].unique():
    bank_reviews = df[df['bank'] == bank]['processed_review'].astype(str)
    
    # Count drivers
    drivers_count[bank] = sum(bank_reviews.str.contains('|'.join(drivers_keywords), case=False))
    
    # Count pain points
    pain_count[bank] = sum(bank_reviews.str.contains('|'.join(pain_keywords), case=False))

print("Drivers count per bank:", drivers_count)
print("Pain points count per bank:", pain_count)



avg_rating = df.groupby('bank')['rating'].mean().sort_values(ascending=False)
print(avg_rating)
