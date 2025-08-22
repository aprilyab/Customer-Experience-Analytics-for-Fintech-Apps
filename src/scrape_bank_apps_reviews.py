from google_play_scraper import Sort, reviews   # pytho package for scrapeing reviews
import pandas as pd


# dictionary for the 3 banks with their app_id and thier name
apps = {
    "Commercial Bank of Ethiopia": "com.combanketh.mobilebanking",
    "Bank of Abyssinia": "com.boa.boaMobileBanking",
    "Dashen Bank": "com.dashen.dashensuperapp"
}

# list to store all 1200 revies from 3 banks
all_reviews = []

# iterate over the dictionary
for bank, app_id in apps.items():
    print(f"Scraping reviews for {bank}...")
    # Initialize an empty list to hold reviews for one app of bank
    bank_reviews = []
    
    # We can fetch in batches of 200; repeat twice to get 400
    for i in range(0, 400, 200):
        batch, _ = reviews(
            app_id,             # app_id of a specific id
            lang='en',
            country='et',
            sort=Sort.NEWEST,   #  sort based on the recenty
            count=200,
            filter_score_with=None,  # Get all ratings from 0 to 5
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

# save the processed data for furture analaysis
df.to_csv("data/raw/raw_bank_apps_reviews.csv", index=False)
print("raw data saved to data/raw/raw_banks_app_reviews.csv")


