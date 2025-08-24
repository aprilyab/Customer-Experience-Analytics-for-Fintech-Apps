import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud



# load the data 
df = pd.read_csv("data/processed/final_bank_apps_review_data.csv")


# Normalize column names
df.columns = df.columns.str.strip().str.lower()

# Sentiment distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='sentiment', hue='sentiment', palette='coolwarm', legend=False)
plt.title("Sentiment Distribution")
plt.savefig("plots/sentiment_distribution.png")
plt.show()

# Rating distribution
plt.figure(figsize=(6, 4))
sns.histplot(df['rating'], bins=5, kde=True)
plt.title("Rating Distribution")
plt.savefig("plots/rating_distribution.png")
plt.show()

# WordCloud for keywords
text = " ".join(df['review'].dropna().astype(str).tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Common Keywords in Reviews")
plt.savefig("plots/wordcloud.png")
plt.show()

# Comparison: CBE vs BOA
# Correct bank names
banks = df[df['bank'].isin(['Commercial Bank of Ethiopia', 'Bank of Abyssinia', 'Dashen Bank'])]

plt.figure(figsize=(6, 4))
sns.boxplot(data=banks, x='bank', y='rating', palette='Set2')
plt.title("Rating Comparison: CBE vs BOA vs Dashen")
plt.ylabel("Rating")
plt.xlabel("Bank")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("plots/bank_rating_comparison.png")
plt.show()


print("✅ Analysis complete. Plots displayed and saved in /plots.")