def fetch_reviews(app_id, bank_name, count=400, country='et'):
    try:
        result, _ = reviews(
            app_id,
            lang='en',
            country=country,  # pass country dynamically
            sort=Sort.NEWEST,
            count=count
        )
    df = fetch_reviews(app_id, bank_name, count=400, country='us')

