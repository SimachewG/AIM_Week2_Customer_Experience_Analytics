# Data Collection and Preprocessing Project

## Introduction
Collecting data from the mobile app has presented several challenges that need to be addressed to ensure effective data analysis and user experience improvement. These challenges include issues related to data accuracy, user consent, and integration with existing data systems.

## Git & Project Setup
- A dedicated GitHub repository was created with a clear structure:
  - `.github/workflows/unittests.yml` for CI automation.
  - `.vscode/settings.json` configured for a consistent development environment.
  - `requirements.txt` populated with dependencies like pandas, google-play-scraper, transformers, spacy, etc.
  - Standardized project folders: `notebook`, `scripts`, `src`, `tests`, etc.
- Git branching strategy implemented:
  - Branch `task-1` created and merged into `main`.
  - Frequent commits with descriptive messages made for key milestones.
- `.gitignore` file added to avoid committing virtual environments, notebook checkpoints, and cache files.

## Web Scraping
- Used `google-play-scraper` to collect review data from the Google Play Store.
- Targeted three banking apps: **CBE**, **BOA**, and **Dashen**.
- Collected:
  - 400+ reviews per bank, totaling over 1,200 reviews.
  - Extracted fields: review, rating, date, app_name, source.

## Preprocessing
- Preprocessing steps implemented in a dedicated script:
  - Duplicates removed.
  - Missing values identified and handled (<5%).
  - Date formats normalized to YYYY-MM-DD.
  - All reviews converted to strings for downstream NLP tasks.
- Exported clean dataset as `bank_reviews.csv` with structure:
  - review, rating, date, bank, source.

### Bank Review Counts After Preprocessing
| Bank  | Total Reviews |
|-------|---------------|
| CBE   | 5521          |
| BOA   | 786           |
| Dashen| 363           |

### Rating Distribution Per Bank
- CBE bank has the highest number of reviews, with the majority being in the 5-star rating category.
- Dashen bank also has a significant number of reviews, mostly in the 5-star category.
- BOA bank has the lowest number of reviews, with a distribution leaning towards 1-star and 5-star ratings.

### Average Rating Per Bank
- BOA: ~2.62
- CBE: ~3.84
- Dashen: ~4.39

## Challenges Faced
- **Integration with Existing Systems:** The collected data needs to be integrated seamlessly with existing databases and analytics tools. Compatibility issues can arise, making it difficult to analyze the data effectively.
- **Data Interpretation:** Interpreting results from an uneven dataset can lead to misinformed decisions, affecting strategic planning and resource allocation.

## Proposed Solutions
- **Utilize APIs for Integration:** Leverage APIs to facilitate the integration of collected data with existing systems.
- **Visual Data Representation:** Use visualizations to illustrate disparities in review counts, helping stakeholders understand potential biases.

## Task 2: Sentiment and Thematic Analysis
### Sentiment Analysis
- Developed a language detection and translation pipeline for multilingual reviews:
  - Used `langdetect` for language detection.
  - Used `translate` library with fallbacks for Microsoft Translator API.
  - Logic: If not English, translate before sentiment analysis.
- Applied `distilbert-base-uncased-finetuned-sst-2-english` via Hugging Face Transformers:
  - Computed `sentiment_label` (Positive/Negative/Neutral).
  - Stored results as `bank_reviews_with_sentiment_themes.csv`.

### Sentiment Analysis Results
| Bank  | Positive | Neutral | Negative |
|-------|----------|---------|----------|
| CBE   | 2988     | 2054    | 478      |
| BOA   | 282      | 308     | 196      |
| Dashen| 263      | 75      | 25       |

### Thematic Analysis
- Text preprocessing: Tokenization, stop word removal, lemmatization using spaCy.
- Keyword extraction via TF-IDF vectorization.
- Manual clustering into themes.

### Advanced Sentiment Analysis with Machine Learning
- Employing models like Naive Bayes improved accuracy by training on labeled data.
- Achieved an accuracy of 77%.

## Task 3: Store Cleaned Data in PostgreSQL
- Created a relational database schema using PostgreSQL to store cleaned customer review data.
- Work Completed:
  - PostgreSQL installed and configured locally.
  - Created database: `bank_reviews`.
  - Defined schema with `banks` and `reviews` tables.
  - Inserted cleaned review data into PostgreSQL using Python (`psycopg2`).
  - Verified 1,000 review records inserted.

## Task 4: Insights and Recommendations
### Insights Extracted
- Top Drivers: "app", "good", "best", "use", "easy".
- Top Pain Points: "crashes", "transaction", "update", "money", "bad".

### Visualizations Created
- Sentiment distribution across banks.
- Average rating per bank.
- Word clouds for positive and negative keywords.

### Ethical Considerations
- Identified possible review bias (e.g., users with bad experiences are more likely to review).

## Problem Encountered
- Difficulties installing Oracle on my local machine. Despite efforts, I was unable to complete the installation.

## Solution Implemented
- Downloaded and installed PostgreSQL, which worked well for my needs.

## Recommendations
- Anyone who can work on this data can try to work with oracle database 
