from sklearn.cluster import KMeans
from stats import *
from document import *

class kmeans:

    def __init__(self, doc):
        self.doc = doc
        self.kmeans = KMeans(n_clusters=20)

    def eval_accuracy(self):
        self.kmeans.fit(self.doc.train, self.doc.labels)
        print self.kmeans.labels_
        labels = self.kmeans.predict(self.doc.test)
        print labels
        correct = 0
        offset = len(self.doc.train)
        for i in range(0, len(labels)):
            print labels[i], self.doc.labels[offset + i],
            correct += 1
        print
        return correct/len(labels)

    def eval_entropy(self):
        self.kmeans.fit(self.doc.data, self.doc.labels)
        ent = get_entropy(self.kmeans.labels_)
        var = get_variance(self.kmeans.labels_)
        return ent, var

    def evaluate(self):
        accuracy = self.eval_accuracy()
        ent, var = self.eval_entropy()
        print 'Accuracy: {}, Entropy: {}, Variance: {}'.format(accuracy, ent, var)
