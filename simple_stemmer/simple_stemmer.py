class SimpleStemmer:
    def __init__(self):
        self.suffixes = [
            'ing', 'ed', 'ly', 'es', 's', 'ment'
        ]

    def stem(self, word):
        for suffix in self.suffixes:
            if word.endswith(suffix):
                return word[:-len(suffix)]
        return word


