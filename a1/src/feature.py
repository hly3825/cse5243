import operator
from tfidf import Tfidf
from output import Output

class Feature:

    def __init__(self):
        self.tfidf = Tfidf()
        self.docs = []
        self.matrix = {}

    def add(self, doc):
        self.docs.append(doc)
        self.tfidf.add(doc)

    def build(self):
        for d in self.docs:
            self.matrix[d.id] = {}
            for w in self.tfidf.wordset:
                self.matrix[d.id][w] = self.tfidf.calc(w, d.id)

class Feature1:

    def __init__(self, f):
        self.tfidf = f.tfidf
        self.docs = f.docs
        self.matrix = f.matrix
        self.out = Output('set1')
        self.features = []

    def _select(self):
        for did, row in self.matrix.iteritems():
            top5 = dict(sorted(row.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
            for word, tfidf in top5.iteritems():
                if tfidf > 0:
                    self.features.append(word)
        self.features = sorted(self.features)

    def dump(self):
        self._select()
        self.out.write_data(self.docs, self.features, self.matrix)

class Feature2(Feature):

    def __init__(self, f):
        self.tfidf = f.tfidf
        self.docs = f.docs

    def generate_weights(self, docs, words):
        pass


