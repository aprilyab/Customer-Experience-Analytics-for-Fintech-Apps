# -----------------------------
# Import dependencies
# -----------------------------
import psycopg2            # PostgreSQL database adapter for Python
import pandas as pd        # For handling and processing CSV data
import os                  # For environment variables and file paths
from dotenv import load_dotenv   # To securely load DB credentials from .env file

# -----------------------------
# Load environment variables from .env file
# (.env should contain host, database, user, password, port)
# -----------------------------
load_dotenv()

host = os.getenv("host")
database = os.getenv("database")
user = os.getenv("user")
password = os.getenv("password")
port = os.getenv("port")

# -----------------------------
# Load the final cleaned review dataset
# -----------------------------
df = pd.read_csv("data/processed/final_bank_apps_review_data.csv")

# -----------------------------
# Connect to PostgreSQL database
# -----------------------------
conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password,
    port=port
)

# Create a cursor object (used to execute SQL commands)
curs = conn.cursor()

# -----------------------------
# Handle Banks Table
# -----------------------------
banks = df["bank"].unique()     # Get unique bank names from dataset
bank_id_map = {}                # Will map each bank name → its database ID

# Dictionary for known banks and their corresponding app IDs
apps = {
    "Commercial Bank of Ethiopia": "com.combanketh.mobilebanking",
    "Bank of Abyssinia": "com.boa.boaMobileBanking",
    "Dashen Bank": "com.dashen.dashensuperapp"
}

# Insert each bank into the Banks table (if not already present)
for bank in banks:
    app_id = apps.get(bank, "unknown_app_id")  # Default app_id if not in dict
    curs.execute(
        """INSERT INTO Banks (bank_name, bank_app_id, country)
           VALUES (%s, %s, %s) 
           ON CONFLICT (bank_name) DO NOTHING
           RETURNING bank_id
        """, (bank, app_id, "Ethiopia")
    )

    # If a new bank was inserted, RETURNING gives us its ID
    result = curs.fetchone()
    if result:
        bank_id = result[0]
    else:
        # If the bank already exists, fetch its ID directly
        curs.execute("SELECT bank_id FROM Banks WHERE bank_name = %s", (bank,))
        bank_id = curs.fetchone()[0]

    # Store mapping: Bank Name → Bank ID
    bank_id_map[bank] = bank_id

# Save inserted banks
conn.commit()

# -----------------------------
# Handle Reviews Table
# -----------------------------
for index, row in df.iterrows():
    curs.execute(
        """INSERT INTO Reviews 
           (bank_id, review, processed_review, rating, date, sentiment, theme, source)
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            bank_id_map[row['bank']],    # link review to correct bank_id
            row['review'],
            row.get('processed_review'),
            int(row['rating']),
            row['date'],
            row.get('sentiment'),
            row.get('theme'),
            row.get('source')
        )
    )

# Save inserted reviews
conn.commit()

# -----------------------------
# Close DB connection
# -----------------------------
curs.close()
conn.close()
