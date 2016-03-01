import math
from sets import Set

class Tfidf:
    def __init__(self):
        self.docs = {}
        self.df = {}

    def add(self, doc):
        tf = {}
        words = doc.title + doc.body
        incr = 1.0/len(words)
        for w in words:
            tf[w] = tf.get(w, 0.0) + incr
        self.docs[doc.id] = tf
        for w in set(words):
            self.df[w] = self.df.get(w, 0) + 1

    def get_tf(self, word, did):
        return self.docs[did].get(word, 0)

    def get_df(self, word):
        return self.df[word]

    def get_tfidf(self, word, did):
        tf = self.get_tf(word, did)
        idf = math.log(len(self.docs)) / (1 + self.get_df(word))
        return tf * idf
