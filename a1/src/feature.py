import operator
from sets import Set
from tfidf import Tfidf
from output import Output

class Feature:

    def __init__(self):
        self.tfidf = Tfidf()
        self.docs = []
        self.twords = Set()
        self.bwords = Set()

    def add(self, doc):
        self.docs.append(doc)
        self.twords.update(doc.title)
        self.bwords.update(doc.body)
        self.tfidf.add(doc)

class Feature1:

    def __init__(self, f):
        self.tfidf = f.tfidf
        self.docs = f.docs
        self.twords = f.twords
        self.bwords = f.bwords
        self.out = Output('set1')
        self.features = Set()
        self.matrix = {}

    def _build(self):
        for d in self.docs:
            self.matrix[d.id] = {}
            words = self.twords | self.bwords
            for w in words:
                self.matrix[d.id][w] = self.tfidf.calc(w, d.id)

    def _select(self):
        for did, row in self.matrix.iteritems():
            top5 = dict(sorted(row.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
            for word, tfidf in top5.iteritems():
                if tfidf > 0:
                    self.features.add(word)
        self.features = sorted(self.features)

    def write(self):
        print 'Building and selecting Feature Set 1'
        self._build()
        self._select()
        self.out.write_data(self.docs, self.features, self.matrix)


class Feature2(Feature):

    def __init__(self, f):
        self.tfidf = f.tfidf
        self.docs = f.docs
        self.twords = f.twords
        self.bwords = f.bwords
        self.out = Output('set2')
        self.features = Set()
        self.matrix = {}

    def _build(self):
        for d in self.docs:
            self.matrix[d.id] = {}
            words = self.twords | self.bwords
            for w in words:
                if w in self.twords:
                    factor = 2.0
                else:
                    factor = 1.0
                self.matrix[d.id][w] = self.tfidf.calc(w, d.id)*factor

    def _select(self):
        for did, row in self.matrix.iteritems():
            top5 = dict(sorted(row.iteritems(), key=operator.itemgetter(1), reverse=True)[:5])
            for word, tfidf in top5.iteritems():
                if tfidf > 0:
                    self.features.add(word)
        self.features = sorted(self.features)

    def write(self):
        print 'Building and selecting Feature Set 2'
        self._build()
        self._select()
        self.out.write_data(self.docs, self.features, self.matrix)

