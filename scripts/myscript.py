# scripts/preprocessing.py
import pandas as pd
from src.core import detect_lang, translate_to_english

def preprocess_reviews(df):
    df['lang'] = df['review'].astype(str).apply(detect_lang)
    df['translated_review'] = df.apply(
        lambda row: translate_to_english(row['review']) if row['lang'] != 'en' else row['review'],
        axis=1
    )
    return df
