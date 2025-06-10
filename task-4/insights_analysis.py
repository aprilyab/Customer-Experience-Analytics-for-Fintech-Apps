# task-4/insights_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load cleaned data
df = pd.read_csv("cleaned_data.csv")

# Sentiment distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='sentiment', palette='coolwarm')
plt.title("Sentiment Distribution")
plt.savefig("plots/sentiment_distribution.png")

# Rating distribution
plt.figure(figsize=(6, 4))
sns.histplot(df['rating'], bins=5, kde=True)
plt.title("Rating Distribution")
plt.savefig("plots/rating_distribution.png")

# WordCloud for keywords (assuming a 'review_text' column)
text = " ".join(df['review_text'].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Common Keywords in Reviews")
plt.savefig("plots/wordcloud.png")

# Comparison: CBE vs BOA
banks = df[df['bank_name'].isin(['CBE', 'BOA'])]
sns.boxplot(data=banks, x='bank_name', y='rating')
plt.title("Rating Comparison: CBE vs BOA")
plt.savefig("plots/bank_rating_comparison.png")

print("Analysis complete. Plots saved in /plots.")
