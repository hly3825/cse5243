import re
from config import *

class Stopper:

    def _read_file(self, filename):
        with open(filename, 'r') as sf:
            return sf.read().split()

    def __init__(self):
        self.stopwords = self._read_file(stopwords_file)
        #self.engwords = self._read_file(engwords_file)

    def filter(self, text):
        text = re.sub('[^A-Za-z]+', ' ', text)
        return [word for word in text.split()
                if len(word) > 3 and
                #word in self.engwords and
                word not in self.stopwords]
