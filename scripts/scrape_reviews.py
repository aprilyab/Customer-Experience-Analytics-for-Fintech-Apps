""" from google_play_scraper import reviews, Sort
import pandas as pd
import os
import datetime

# Create directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# App package names
APP_IDS = {
    "Commercial Bank of Ethiopia": "com.combanketh.mobilebanking",
    "Bank of Abyssinia": "com.boa.boaMobileBanking",
    "Dashen Bank": "com.dashen.dashensuperapp"
}

def fetch_reviews(app_id, bank_name, count=400):
    try:
        # All banks from Ethiopia store
        result, _ = reviews(
            app_id,
            lang='en',
            country='et',  # Ethiopia
            sort=Sort.NEWEST,
            count=count
        )

        if not result:
            print(f"[WARNING] No reviews found for {bank_name} ({app_id})")
            return pd.DataFrame()

        print(f"[INFO] Fetched {len(result)} reviews for {bank_name}")

        df = pd.DataFrame(result)

        if not {'content', 'score', 'at'}.issubset(df.columns):
            print(f"[ERROR] Missing expected keys in review data for {bank_name}. Available keys: {list(df.columns)}")
            return pd.DataFrame()

        # Process DataFrame
        df = df[['content', 'score', 'at']]
        df.rename(columns={'content': 'review', 'score': 'rating', 'at': 'date'}, inplace=True)
        df['bank'] = bank_name
        df['source'] = 'Google Play'

        # Print sample reviews
        print(f"[DEBUG] Sample reviews for {bank_name}:")
        print(df.head(3).to_string(index=False))

        return df

    except Exception as e:
        print(f"[ERROR] Failed to fetch reviews for {bank_name} ({app_id}): {e}")
        return pd.DataFrame()

# Collect all reviews
all_reviews = pd.DataFrame()

for bank, app_id in APP_IDS.items():
    print(f"\nFetching reviews for {bank}")
    df = fetch_reviews(app_id, bank)
    print(f"[DEBUG] Shape for {bank}: {df.shape}")
    if not df.empty:
        all_reviews = pd.concat([all_reviews, df], ignore_index=True)
    else:
        print(f"[SKIPPED] No usable reviews for {bank}")

# Save to CSV with timestamp
if not all_reviews.empty:
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"data/raw_reviews_{timestamp}.csv"
    all_reviews.to_csv(filename, index=False)
    print(f"[SUCCESS] Scraping complete. {len(all_reviews)} reviews saved to {filename}")
else:
    print("[FAILURE] No reviews were collected.")
    """


    




from google_play_scraper import Sort, reviews
import pandas as pd

apps = {
    "Commercial Bank of Ethiopia": "com.combanketh.mobilebanking",
    "Bank of Abyssinia": "com.boa.boaMobileBanking",
    "Dashen Bank": "com.dashen.dashensuperapp"
}

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

# Drop duplicates and missing data
df.drop_duplicates(subset=['review'], inplace=True)
df.dropna(subset=['review', 'rating'], inplace=True)

# Save to CSV for next steps
df.to_csv("bank_reviews.csv", index=False)
print("Saved scraped reviews to bank_reviews.csv")

