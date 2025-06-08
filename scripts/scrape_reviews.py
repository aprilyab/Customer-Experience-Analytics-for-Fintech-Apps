from google_play_scraper import Sort, reviews
import pandas as pd

apps = {
    "Commercial Bank of Ethiopia": "com.combanketh.mobilebanking",
    "Bank of Abyssinia": "com.boa.boaMobileBanking",
    "Dashen Bank": "com.dashen.dashensuperapp"
} ...

all_reviews = []

for bank, package_name in apps.items():
    print(f"Scraping reviews for {bank}...")
    # Initialize an empty list to hold reviews for this app
    bank_reviews = []

    # We can fetch in batches of 200; repeat twice to get 400
    for i in range(0, 400, 200):
        batch, _ = reviews(
            package_name,
            lang='en',
            country='us',
            sort=Sort.NEWEST,
            count=200,
            filter_score_with=None,  # Get all ratings
            continuation_token=None if i == 0 else continuation_token
        )
        bank_reviews.extend(batch)
        # Save continuation token for next batch
        continuation_token = _ if _ else None
        if continuation_token is None:
            break
    
    # Format reviews to dicts with needed info
    for r in bank_reviews:
        all_reviews.append({
            "review": r['content'],
            "rating": r['score'],
            "date": r['at'].strftime("%Y-%m-%d"),
            "bank": bank,
            "source": "Google Play"
        })

# Convert to DataFrame
df = pd.DataFrame(all_reviews)
print(f"Total reviews scraped: {len(df)}")
task-1
# Drop duplicates and missing data
df.drop_duplicates(subset=['review'], inplace=True)
df.dropna(subset=['review', 'rating'], inplace=True)

# Save to CSV for next steps
df.to_csv("bank_reviews.csv", index=False)
print("Saved scraped reviews to bank_reviews.csv")

