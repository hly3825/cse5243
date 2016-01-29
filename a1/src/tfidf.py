import math

class Tfidf:
    def __init__(self):
        self.docs = {}
        self.words = {}

    def _idf(self, word):
        return math.log(len(self.docs)) / (1 + self.words[word])

    def add(self, doc):
        words = doc.title + doc.body
        tf = {}
        for w in words:
            tf[w] = (tf.get(w, 0.0) + 1.0)/len(words)
            self.words[w] = self.words.get(w, 0) + 1
        self.docs[doc.id] = tf
        print "added document %s" % doc.id

    def calc(self, word, id):
        return self.docs[id][word] * self._idf(word)

    def pp(self, id):
        d = self.docs[id]
        for w in d.keys():
            print w, self.calc(w, id)
