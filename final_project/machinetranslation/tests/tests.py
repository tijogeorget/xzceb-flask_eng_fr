import unittest
from translator import englishtofrench, frenchtoenglish
class TestMyModule(unittest.TestCase):
    def test_englishtofrench(self):
        self.assertEqual(englishtofrench('Hello'), 'Bonjour')
    def test_frenchtoenglish(self):
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()
    