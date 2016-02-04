import operator
from sets import Set
from tfidf import Tfidf
from output import Output

class Feature:

    def __init__(self):
        self.tfidf = Tfidf()
        self.docs = []
        self.words = []
        self.title = Set()
        self.body = Set()
        self.topics = Set()
        self.places = Set()
        self.matrix = {}
        self.idfs = {}

    def add(self, doc):
        self.docs.append(doc)
        self.tfidf.add(doc)
        self.title.update(doc.title)
        self.body.update(doc.body)
        self.topics.update(doc.topics)
        self.places.update(doc.places)

    def _compress(self):
        self.title = list(self.title)
        self.body = list(self.body)
        self.topics = list(self.topics)
        self.places = list(self.places)
        self.words = self.title + self.body + self.topics + self.places
        self.title = []
        self.body = []

    def build(self):
        self._compress()
        print 'Building tf-idf matrix'
        for d in self.docs:
            self.matrix[d.id] = {}
            for w in self.words:
                idf = self.tfidf.get_idf(w)
                if idf > 2:
                    self.idfs[w] = idf
                    self.matrix[d.id][w] = self.tfidf.get_tfidf(w, d.id)
                else:
                    self.words.remove(w)

class Feature1:

    def __init__(self, f):
        self.f = f
        self.tfidf = f.tfidf
        self.matrix = f.matrix
        self.idfs = f.idfs
        self.out = Output('output1')
        self.features = Set()

    def _select(self):
        nonzero = {}
        for did, row in self.matrix.iteritems():
            nonzero.update({k:v for (k,v) in row.iteritems() if v>0})
        length = len(nonzero)
        start = max(length/2 - 75, 0)
        end   = min(length/2 + 25, length)
        selected = dict(sorted(nonzero.iteritems(),
                        key=operator.itemgetter(1),
                        reverse=True)[start:end])
        for word, tfidf in selected.iteritems():
            self.features.add(word)
        self.features = sorted(self.features)
        self.features += self.f.topics
        self.features += self.f.places

    def write(self):
        print 'Building and selecting Feature Set 1'
        self._select()
        self.out.write_data(self.f.docs, self.features, self.matrix)


class Feature2(Feature):

    def __init__(self, f):
        self.f = f
        self.tfidf = f.tfidf
        self.matrix = f.matrix
        self.idfs = f.idfs
        self.out = Output('output2')
        self.features = Set()

    def _select(self):
        idfs = {k:v for (k,v) in self.idfs.iteritems() if v>1}
        length = len(idfs)
        start = max(length/2 - 80, 0)
        end   = min(length/2 + 20, length)
        selected = dict(sorted(idfs.iteritems(),
                        key=operator.itemgetter(1),
                        reverse=True)[start:end])
        for word, idf in selected.iteritems():
            self.features.add(word)
        self.features = sorted(self.features)
        self.features += self.f.topics
        self.features += self.f.places

    def write(self):
        print 'Building and selecting Feature Set 2'
        self._select()
        self.out.write_data(self.f.docs, self.features, self.matrix)

