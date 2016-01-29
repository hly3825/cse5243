import re

class Stopper:

    def __init__(self, filename):
        self.stopwords = []
        with open(filename, 'r') as sf:
            self.stopwords = sf.read().split()

    def filter(self, text):
        text = re.sub('[^A-Za-z]+', ' ', text)
        return [word for word in text.split() if word not in self.stopwords]
