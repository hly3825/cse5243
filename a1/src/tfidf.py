import math, numpy
from collections import Counter
from sets import Set
from output import *

class Tfidf:
    def __init__(self):
        self.docs = []
        self.wordset = Set()
        self.df = Counter()
        self.idfmat = []

    def add(self, doc):
        self.docs.append(doc)
        words = doc.title + doc.body
        for w in Set(words):
            self.wordset.add(w)
            self.df[w] += 1

    def _filter(self):
        self.wordset = [w for w in self.wordset if self.df[w] > 1]

    def _tf(self, word, doc):
        words = doc.title + doc.body
        return words.count(word)

    def _tfmat(self):
        for d in self.docs:
            tfvec = [self._tf(w, d) for w in self.wordset]
            yield d.id, tfvec

    def _idf(self, word):
        return math.log(len(self.docs)) / (1 + self.df[word])

    def _idfmat(self):
        idfvec = [self._idf(w) for w in self.wordset]
        idfmat = numpy.zeros((len(idfvec), len(idfvec)))
        numpy.fill_diagonal(idfmat, idfvec)
        self.idfmat = idfmat

    def _tfidfmat(self):
        for id, tfvec in self._tfmat():
            yield id, numpy.dot(tfvec, self.idfmat)

    def _print_wordset(self):
        set_output('wordset')
        for w in self.wordset:
            print str(w)
        reset_output()

    def dump(self):
        self._filter()
        self._idfmat()
        self._print_wordset()
        set_output('tfidf')
        numpy.set_printoptions(precision=3)
        for id, row in self._tfidfmat():
            print id, row
        reset_output()
