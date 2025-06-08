from google_play_scraper import reviews, Sort

sample_reviews, _ = reviews(
    'com.ethiopia.cbe',  # CBE package name
    lang='en',
    country='us',
    sort=Sort.NEWEST,
    count=2
)

for r in sample_reviews:
    print(r['content'], r['score'], r['at'])
