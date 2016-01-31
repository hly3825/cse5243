import math

class Tfidf:
    def __init__(self):
        self.docs = {}
        self.words = {}

    def add(self, doc):
        words = doc.title + doc.body
        tf = {}
        for w in words:
            tf[w] = (tf.get(w, 0.0) + 1.0)/len(words)
            self.words[w] = self.words.get(w, 0) + 1
        self.docs[doc.id] = tf

    def _idf(self, word):
        return math.log(len(self.docs)) / (1 + self.words[word])

    def _calc(self, word, id):
        return self.docs[id][word] * self._idf(word)

    def dump(self):
        for d in self.docs.keys():
            print d
            for w in self.docs[d].keys():
                f = self._calc(w, d)
            print
