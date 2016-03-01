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
        self.dfs = {}

    def add(self, doc):
        if not doc.topics:
            return
        self.docs.append(doc)
        self.tfidf.add(doc)
        self.title.update(doc.title)
        self.body.update(doc.body)
        self.topics.update(doc.topics)
        self.places.update(doc.places)

    def _compress(self):
        self.title = list(self.title)
        self.body = list(self.body)
        self.topics = sorted(self.topics)
        self.places = sorted(self.places)
        self.words = self.title + self.body
        self.title = []
        self.body = []

    def build(self):
        self._compress()
        print 'Building tf-idf matrix'
        for d in self.docs:
            self.matrix[d.id] = {}
        for w in self.words:
            df = self.tfidf.get_df(w)
            if df > 2:
                self.dfs[w] = df
                for d in self.docs:
                    tfidf = self.tfidf.get_tfidf(w, d.id)
                    if tfidf:
                        self.matrix[d.id][w] = tfidf
        self.words = []

class Feature1:

    def __init__(self, f):
        self.f = f
        self.tfidf = f.tfidf
        self.matrix = f.matrix
        self.dfs = f.dfs
        self.out = Output('output1')
        self.features = Set()

    def _select(self):
        values = []
        for did, row in self.matrix.iteritems():
            values += [(v,k) for (k,v) in row.iteritems()]
        length = len(values)
        start = min(length/20, 100)
        end   = min(start+1000, length)
        selected = sorted(values,
                        key=operator.itemgetter(0),
                        reverse=True)[start:end]
        for tfidf, word in selected:
            self.features.add(word)
        self.features = sorted(self.features)

    def write(self):
        print 'Building and selecting Feature Set 1'
        self._select()
        self.out.write_data(self.f.docs, self.features, self.matrix)


class Feature2(Feature):

    def __init__(self, f):
        self.f = f
        self.tfidf = f.tfidf
        self.matrix = f.matrix
        self.dfs = f.dfs
        self.out = Output('output2')
        self.features = Set()

    def _select(self):
        length = len(self.dfs)
        start = min(length/20, 100)
        end   = min(start+1000, length)
        selected = sorted(self.dfs.iteritems(),
                        key=operator.itemgetter(1),
                        reverse=True)[start:end]
        for word, idf in selected:
            self.features.add(word)
        self.features = sorted(self.features)

    def write(self):
        print 'Building and selecting Feature Set 2'
        self._select()
        self.out.write_data(self.f.docs, self.features, self.matrix)

