import mysql.connector
import pandas as pd

df = pd.read_csv('bank_reviews_cleaned.csv')

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Henokmysql@415',
    database='bank_reviews'
)
cursor = conn.cursor()

# Insert banks and store their IDs
bank_map = {}
banks = df[['bank', 'source']].drop_duplicates()

for _, row in banks.iterrows():
    cursor.execute("INSERT INTO banks (name, source) VALUES (%s, %s)", (row['bank'], row['source']))
    conn.commit()
    bank_map[(row['bank'], row['source'])] = cursor.lastrowid

# Insert reviews
for _, row in df.iterrows():
    bank_id = bank_map[(row['bank'], row['source'])]
    cursor.execute(
        "INSERT INTO reviews (review_text, rating, review_date, bank_id) VALUES (%s, %s, %s, %s)",
        (row['review'], row['rating'], row['date'], bank_id)
    )

conn.commit()
cursor.close()
conn.close()
print("the data inserted successfuly")
