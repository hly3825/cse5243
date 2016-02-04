import operator
from sets import Set
from tfidf import Tfidf
from output import Output

class Feature:

    def __init__(self):
        self.tfidf = Tfidf()
        self.docs = []
        self.title = Set()
        self.body = Set()
        self.topics = Set()
        self.places = Set()

    def add(self, doc):
        self.docs.append(doc)
        self.tfidf.add(doc)
        self.title.update(doc.title)
        self.body.update(doc.body)
        self.topics.update(doc.topics)
        self.places.update(doc.places)

class Feature1:

    def __init__(self, f):
        self.tfidf = f.tfidf
        self.docs = f.docs
        self.title = f.title
        self.topics = f.topics
        self.places = f.places
        self.body = f.body
        self.out = Output('output1')
        self.features = Set()
        self.matrix = {}

    def _build(self):
        for d in self.docs:
            self.matrix[d.id] = {}
            words = self.title | self.body | self.topics | self.places
            for w in words:
                self.matrix[d.id][w] = self.tfidf.get_tfidf(w, d.id)

    def _select(self):
        for did, row in self.matrix.iteritems():
            selected = dict(sorted(row.iteritems(),
                            key=operator.itemgetter(1),
                            reverse=True)[2:7])
            for word, tfidf in selected.iteritems():
                if tfidf > 0:
                    self.features.add(word)
        self.features.update(self.topics)
        self.features.update(self.places)

    def write(self):
        print 'Building and selecting Feature Set 1'
        self._build()
        self._select()
        self.out.write_data(self.docs, self.features, self.matrix)


class Feature2(Feature):

    def __init__(self, f):
        self.tfidf = f.tfidf
        self.docs = f.docs
        self.title = f.title
        self.body = f.body
        self.topics = f.topics
        self.places = f.places
        self.out = Output('output2')
        self.features = Set()
        self.matrix = {}
        self.idfs = {}

    def _build(self):
        for d in self.docs:
            self.matrix[d.id] = {}
            words = self.title | self.body | self.topics | self.places
            for w in words:
                self.matrix[d.id][w] = self.tfidf.get_tfidf(w, d.id)
                self.idfs[w] = self.tfidf.get_idf(w)

    def _select(self):
        self.idfs = {k:v for (k,v) in self.idfs.iteritems() if v>1}
        length = len(self.idfs)
        start = max(length/2 - 50, 0)
        end   = min(length/2 + 50, length)
        selected = dict(sorted(self.idfs.iteritems(),
                        key=operator.itemgetter(1),
                        reverse=True)[start:end])
        for word, idf in selected.iteritems():
            self.features.add(word)
        self.features.update(self.topics)
        self.features.update(self.places)

    def write(self):
        print 'Building and selecting Feature Set 2'
        self._build()
        self._select()
        self.out.write_data(self.docs, self.features, self.matrix)

