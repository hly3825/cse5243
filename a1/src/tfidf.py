import math
from sets import Set

class Tfidf:
    def __init__(self):
        self.docs = {}
        self.df = {}
        self.wordset = Set()

    def add(self, doc):
        tf = {}
        words = doc.title + doc.body
        incr = 1.0/len(words)
        for w in words:
            tf[w] = tf.get(w, 0.0) + incr
        self.docs[doc.id] = tf
        for w in set(words):
            self.wordset.add(w)
            self.df[w] = self.df.get(w, 0) + 1

    def calc(self, word, did):
        tf = self.docs[did].get(word, 0)
        idf = math.log(len(self.docs)) / (1 + self.df[word])
        return tf * idf
