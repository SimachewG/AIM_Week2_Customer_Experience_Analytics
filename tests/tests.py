# tests/test_core.py
import unittest
from src.core import detect_lang, translate_to_english

class TestTranslation(unittest.TestCase):

    def test_detect_lang(self):
        self.assertEqual(detect_lang("Hello"), "en")
        self.assertNotEqual(detect_lang("ጤና ይስጥልኝ"), "en")

    def test_translate_to_english(self):
        result = translate_to_english("Bonjour")
        self.assertIsInstance(result, str)
        self.assertNotEqual(result, "Bonjour")

if __name__ == "__main__":
    unittest.main()
