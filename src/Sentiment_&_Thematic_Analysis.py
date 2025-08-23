# import dependensies
import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer



# packages for sentiment analaysis
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# load the processed review
df=pd.read_csv("data/processed/processed_banks_app_reviews.csv")



# download NLTK resources
nltk.download("punket")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download('punkt_tab')
nltk.download('vader_lexicon')


# preprocessing the data
"""
Steps:
-- Clean text: Remove punctuation, special characters, convert to lowercase.
-- Tokenize: Split text into words.
-- Remove stop words: Eliminate common words (e.g., "the," "and").
-- Lemmatize: Reduce words to base form (e.g., "running" → "run").

"""
# define function for processing the review before sentiment analaysis
def preprocess_text(text):
    text=text.lower()  # change to lowercase
    text=text.translate(str.maketrans("","",string.punctuation))  # remove punctuations
    tokens=word_tokenize(text) # tokenize the text to split apart the text
    lemmatizer=WordNetLemmatizer()
    stop_words=set(stopwords.words("english"))
    tokens=[lemmatizer.lemmatize(word) for word in tokens if word.isalnum() and word not in stop_words]
    return " ".join(tokens)

# Apply preprocessing to the review column
df["processed_review"]=df["review"].apply(preprocess_text)

# sentiment analaysis with VADER
# define an object
sis=SentimentIntensityAnalyzer()

def get_sentiment(text):
    scores=sis.polarity_scores(text)
    if scores["compound"]> 0.05:
        return "positive"
    elif scores["compound"]< -0.05:
        return "negative"
    else:
        return "neutral"

# apply the get_sentiment on the review column   
df["sentiment"]=df["processed_review"].apply(get_sentiment)
# count the frequency of each sentiment type
print(df["sentiment"].value_counts()) 

# Keyword Extraction
# Vectorize the dataset
vectorizer=TfidfVectorizer(max_features=100)
x=vectorizer.fit_transform(df["processed_review"])

# get tok keywords
keywords=vectorizer.get_feature_names_out()


# Manual/Rule-Based Clustering
# Group related keywords
themes = {
    "Account Access & Security": [
        "access", "account", "login", "secure", "security", "issue", "problem", "cant", "open"
    ],
    "Transactions & Payments": [
        "transaction", "transfer", "payment", "bill", "money", "system", "slow", "fast", "reliable"
    ],
    "User Experience & Interface": [
        "app", "application", "apps", "mobile", "user", "userfriendly", "easy", "simple", "friendly",
        "seamless", "smooth", "convenient", "experience", "design", "interface"
    ],
    "Customer Service & Support": [
        "customer", "service", "support", "help", "please", "developer", "fix"
    ],
    "Feature Requests & Updates": [
        "feature", "update", "option", "need", "new", "better", "improvement"
    ]
}

# define function to assign themes for each row of reviwe

# phrases into themes per bank
def assign_review(review):
    for theme,keywords in themes.items():
        if any(keyword in review for keyword in keywords ):
            return theme
        else:
            return "other"
        
# apply assign_review on the df
df["theme"]=df["processed_review"].apply(assign_review)

