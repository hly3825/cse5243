from sklearn.cluster import KMeans
from stats import *
from document import *

class kmeans:

    def __init__(self, doc):
        self.doc = doc
        self.kmeans = KMeans(n_clusters=10)

    def evaluate(self):
        self.kmeans.fit(self.doc.train)
        print self.kmeans.labels_
        print self.kmeans.predict(self.doc.test)
