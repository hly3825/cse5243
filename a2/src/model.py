import time
from stats import *
from document import *

class model:

    def __init__(self, doc, algo):
        self.doc = doc
        self.algo = algo

    def eval_performance(self):
        start = time.time()
        self.algo.fit(self.doc.data)
        end = time.time()
        return end - start

    def eval_accuracy(self):
        labels = self.algo.labels_
        print labels
        correct = 0
        for i in range(0, len(labels)):
            print labels[i], self.doc.labels[i],
            correct += 1
        print
        return correct/len(labels)

    def eval_entropy(self):
        ent = get_entropy(self.algo.labels_)
        var = get_variance(self.algo.labels_)
        return ent, var

    def evaluate(self):
        perf = self.eval_performance()
        accuracy = self.eval_accuracy()
        ent, var = self.eval_entropy()
        print 'Time: {}, Accuracy: {}, '.format(perf, accuracy),
        print 'Entropy: {}, Variance: {}'.format(ent, var)
