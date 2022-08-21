from translator import english_to_french, french_to_english
import unittest

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Mon amour'),'My Love')
        self.assertEqual(french_to_english(''),'Empty')
        self.assertNotEqual(french_to_english('Fleur'),'Flow')
        

class TestEnglishToFrench(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(english_to_french('My Love'),'Mon amour')
        self.assertEqual(english_to_french(''),'Empty')
        self.assertNotEqual(english_to_french('School'),'Lecole')
unittest.main()
