import time
import numpy as np
from document import *
from collections import Counter
from sklearn.metrics.cluster import *

class model:

    def __init__(self, doc, algo):
        self.doc = doc
        self.algo = algo

    def eval_performance(self):
        start = time.time()
        self.algo.fit(self.doc.data)
        end = time.time()
        print 'Time taken: {}'.format(end - start)

    def eval_topics(self):
        labels = self.algo.labels_
        cmax = max(labels)
        actuals = {}
        avg = 0.0
        for i in range(0, cmax):
            group = np.where(labels == i)[0]
            actuals[i] = [self.doc.labels[j] for j in group]
            #print i, actuals[i]
            avg += entropy(actuals[i])*len(actuals[i])
        print 'Topical Entropy: {}'.format(avg/len(labels))

    def eval_internal(self):
        ent = entropy(self.algo.labels_)
        var = np.var(self.algo.labels_)
        print 'Entropy: {}, Variance: {}'.format(ent, var)

    def eval_ground(self):
        cmpl = completeness_score(self.doc.labels, self.algo.labels_)
        homo = homogeneity_score(self.doc.labels, self.algo.labels_)
        vscore = v_measure_score(self.doc.labels, self.algo.labels_)
        mutual = normalized_mutual_info_score(self.doc.labels, self.algo.labels_)
        print 'Completeness: {}, Homogeneity: {}'.format(cmpl, homo)
        print 'V-Measure: {}, Mutual Info: {}'.format(vscore, mutual)

    def evaluate(self):
        self.eval_performance()
        self.eval_topics()
        self.eval_internal()
        self.eval_ground()
        print

