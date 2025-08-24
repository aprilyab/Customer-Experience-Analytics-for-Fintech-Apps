# Customer Experience Analytics for Fintech Apps
**Customer Experience Analytics for Fintech Apps**
**Date:** 04 June – 10 June 2025  

---

## Table of Contents

- [Customer Experience Analytics for Fintech Apps](#customer-experience-analytics-for-fintech-apps)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Business Objective](#business-objective)
  - [Scenarios](#scenarios)
    - [Scenario 1: Retaining Users](#scenario-1-retaining-users)
    - [Scenario 2: Enhancing Features](#scenario-2-enhancing-features)
    - [Scenario 3: Managing Complaints](#scenario-3-managing-complaints)
  - [Dataset Overview](#dataset-overview)
  - [Project Setup](#project-setup)
  - [Methodology](#methodology)
    - [Data Collection \& Preprocessing](#data-collection--preprocessing)
    - [Sentiment Analysis](#sentiment-analysis)
    - [Thematic Analysis](#thematic-analysis)
    - [Database Storage](#database-storage)
  - [Insights \& Recommendations](#insights--recommendations)
    - [Ratings Overview](#ratings-overview)
    - [Drivers (Positive Factors)](#drivers-positive-factors)
    - [Pain Points (Negative Factors)](#pain-points-negative-factors)
    - [Recommendations](#recommendations)
  - [Visualizations](#visualizations)
  - [References](#references)
  - [License \& Acknowledgments](#license--acknowledgments)

---

## Project Overview

This project focuses on analyzing **customer satisfaction with mobile banking apps** by collecting and processing user reviews from the Google Play Store for three Ethiopian banks:

- Commercial Bank of Ethiopia (CBE)  
- Bank of Abyssinia (BOA)  
- Dashen Bank  

The goal is to **scrape app reviews, analyze sentiment and themes, and visualize insights**, simulating the role of a Data Analyst at **Omega Consultancy**, a firm advising banks.  

Building on Week 1’s foundational skills, this challenge introduces:  

- Web scraping  
- Thematic NLP analysis  
- Basic database engineering  

---

## Business Objective

Omega Consultancy supports banks in improving their mobile apps to enhance **customer retention and satisfaction**.  

As a Data Analyst, responsibilities include:  

- Scraping user reviews from the Google Play Store.  
- Analyzing sentiment (positive/negative/neutral) and extracting themes (e.g., “bugs”, “UI”).  
- Identifying satisfaction drivers (e.g., speed) and pain points (e.g., crashes).  
- Storing cleaned review data in an **Oracle database**.  
- Delivering a report with visualizations and actionable recommendations.  

---

## Scenarios

These scenarios simulate real consulting tasks faced by banking product, marketing, and engineering teams:

### Scenario 1: Retaining Users
- CBE has a 4.4-star rating, BOA 2.8, and Dashen 4.0.  
- Users report **slow loading during transfers**.  
- Task: Analyze if this is a broader issue and suggest areas for app investigation.

### Scenario 2: Enhancing Features
- Extract desired features through keyword and theme extraction (e.g., **transfer, fingerprint login, faster loading times**).  
- Task: Recommend how each bank can stay competitive in app functionality.

### Scenario 3: Managing Complaints
- Cluster and track complaints such as **“login error”**.  
- Task: Guide **AI chatbot integration** and improve support resolution strategies.  

These scenarios focus on:  

- **User retention**  
- **Feature innovation**  
- **Support efficiency**  

Directory Structure
Customer-Experience-Analytics-for-Fintech-Apps/
│── data/
│   ├── raw/               # Raw scraped reviews
│   ├── processed/         # Cleaned and transformed reviews
│── notebooks/
│   ├── data_collection/   # Scripts to scrape reviews
│   ├── analysis/          # Sentiment, keywords, themes
│   ├── database/          # Queries & database tests
│   └── reporting/         # Visualizations and plots
│── src/
│   ├── scraping/          # Scripts for web scraping
│   ├── preprocessing/     # Cleaning, normalization, tokenization
│   ├── analysis/          # Sentiment & thematic analysis
│   ├── database/          # PostgreSQL/Oracle storage scripts
│   └── visualization/     # Plots & dashboards
│── tests/
│   ├── scraping/
│   ├── preprocessing/
│   ├── analysis/
│   └── database/
│── .gitignore
│── requirements.txt
│── README.md

## Dataset Overview

**Source:** Google Play Store  

**Collected Data:**  

| Column            | Description                                     |
|------------------|-------------------------------------------------|
| review            | User feedback (text)                            |
| rating            | 1–5 stars                                       |
| date              | Review posting date                              |
| bank              | Bank name                                       |
| source            | Google Play                                     |
| processed_review  | Cleaned and tokenized review text               |
| sentiment         | Positive, neutral, or negative                  |
| theme             | Assigned theme (e.g., UI, Transaction issues)  |

**Minimum Reviews:** 400 per bank (total ~1,200)  

---

## Project Setup

1. **Environment:** Python 3.x, PostgreSQL or Oracle XE  
2. **Dependencies:**  
   - `pandas`, `numpy`  
   - `google-play-scraper`  
   - `scikit-learn`, `spacy`  
   - `psycopg2` or `oracledb`  
   - `matplotlib`, `seaborn`, `wordcloud`  
   - `transformers`, `vaderSentiment`, `textblob`  
3. **Database:**  
   - `Banks` table stores bank information  
   - `Reviews` table stores processed reviews  
4. **Data Storage:** Cleaned review data linked with `bank_id`  

---

## Methodology

### Data Collection & Preprocessing
- Scraped reviews, ratings, and dates for CBE, BOA, and Dashen Bank.  
- Normalized dates, removed duplicates, and handled missing values.  
- Saved processed data in CSV for reproducibility.

### Sentiment Analysis
- Applied NLP models (e.g., DistilBERT or VADER) for labeling sentiment.  
- Classified each review as positive, neutral, or negative.  
- Aggregated sentiment scores by bank and rating.

### Thematic Analysis
- Extracted keywords using TF-IDF and spaCy.  
- Clustered keywords into 3–5 recurring themes per bank (e.g., **Account Access, Transaction Performance, UI/UX, Customer Support, Feature Requests**).  
- Assigned each review to a theme programmatically.

### Database Storage
- Designed relational schema with `Banks` and `Reviews` tables.  
- Inserted unique banks and linked reviews via `bank_id`.  
- Handled duplicates safely using parameterized queries.

---

## Insights & Recommendations

### Ratings Overview
| Bank                        | Average Rating |
|------------------------------|---------------|
| Dashen Bank                  | 4.24          |
| Commercial Bank of Ethiopia  | 3.95          |
| Bank of Abyssinia            | 2.98          |

### Drivers (Positive Factors)
- **Dashen Bank:** Fast app performance, intuitive UI, seamless transfers  
- **CBE:** Wide feature set, reliable updates, easy-to-use mobile banking  
- **BOA:** Friendly UI for basic functions, consistent design  

### Pain Points (Negative Factors)
- **Dashen Bank:** Occasional crashes during updates  
- **CBE:** Slow transfers, delayed response times  
- **BOA:** Frequent login issues, app instability, poor support  

### Recommendations
- **Dashen Bank:** Crash reporting, budgeting tools, multi-language support  
- **CBE:** Faster transfers, biometric authentication, simplify navigation  
- **BOA:** Improve stability, strengthen support, introduce essential features  

---

## Visualizations
- Rating distribution per bank  
- Sentiment trends over time  
- Keyword clouds  
- Theme distribution per bank  
- Comparative insights for stakeholders  

All plots saved in `plots/` folder.

---
---

## References
- **Web Scraping:** [google-play-scraper](https://github.com/JoMingyu/google-play-scraper)  
- **Data Handling:** [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)  
- **Sentiment Analysis:** [Hugging Face Transformers](https://huggingface.co/docs/transformers/main_classes/pipelines#transformers.TextClassificationPipeline), [VADER](https://github.com/cjhutto/vaderSentiment), [TextBlob](https://textblob.readthedocs.io/en/dev/)  
- **Thematic Analysis:** [spaCy](https://spacy.io/usage/spacy-101), [Scikit-learn TF-IDF](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)  
- **Database:** [Oracle XE](https://www.oracle.com/database/technologies/xe-downloads.html), [psycopg2](https://www.psycopg.org/), [oracledb](https://python-oracledb.readthedocs.io/en/latest/)  

---

## License & Acknowledgments
- Developed for 10 Academy AI Mastery Week 2 Challenge.  
- Licensed under MIT for educational purposes.  
- Special thanks to facilitators and mentors.  

---

**AUTHOR**
Name: Henok Yoseph
Email: henokapril@gmail.com
Github: [http// april.com](https://github.com/aprilyab)
