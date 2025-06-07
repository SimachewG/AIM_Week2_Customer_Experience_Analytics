# src/core.py
from langdetect import detect
from translate import Translator

def detect_lang(text):
    try:
        return detect(str(text))
    except:
        return "unknown"

def translate_to_english(text):
    try:
        if not isinstance(text, str) or text.strip() == "":
            return text
        return Translator(to_lang="en").translate(text)
    except Exception:
        return text
