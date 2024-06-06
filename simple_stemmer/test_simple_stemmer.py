import unittest
from simple_stemmer import SimpleStemmer

class TestSimpleStemmer(unittest.TestCase):

    def setUp(self):
        self.stemmer = SimpleStemmer()

    def test_stem_removes_ing(self):
        self.assertEqual(self.stemmer.stem('running'), 'runn')

    def test_stem_removes_ed(self):
        self.assertEqual(self.stemmer.stem('stopped'), 'stopp')

    def test_stem_removes_ly(self):
        self.assertEqual(self.stemmer.stem('happily'), 'happi')

    def test_stem_removes_es(self):
        self.assertEqual(self.stemmer.stem('houses'), 'hous')

    def test_stem_removes_s(self):
        self.assertEqual(self.stemmer.stem('cats'), 'cat')

    def test_stem_removes_ment(self):
        self.assertEqual(self.stemmer.stem('argument'), 'argu')

    def test_stem_removes_able(self):
        self.assertEqual(self.stemmer.stem('enjoyable'), 'enjoy')

    def test_stem_no_change(self):
        self.assertEqual(self.stemmer.stem('cat'), 'cat')

    def test_stem_no_change_two(self):
        self.assertEqual(self.stemmer.stem('less'), 'less')

if __name__ == '__main__':
    unittest.main()
