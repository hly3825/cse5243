import math

class Tfidf:
    def __init__(self):
        self.docs = {}
        self.words = {}

    def add(self, doc):
        tf = {}
        words = doc.title + doc.body
        for w in words:
            tf[w] = (tf.get(w, 0.0) + 1.0)/len(words)
            self.words[w] = self.words.get(w, 0) + 1
        self.docs[doc.id] = tf

    def _idf(self, word):
        return math.log(len(self.docs)) / (1 + self.words[word])

    def dump(self):
        for id, tfs in self.docs.iteritems():
            print id,
            for w, tf in tfs.iteritems():
                tf_idf = tf * self._idf(w)
                print (str(w), tf_idf),
            print "\n\n"
