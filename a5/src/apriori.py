import operator
import numpy as np
import itertools as it
from collections import Counter
from transaction import *

class apriori:

    def __init__(self, txns):
        self.txns = []
        self.itemset = set()
        self.labels = set()
        for t in txns:
            self.labels.update(t.labels)
            txn = frozenset(t.features+t.labels)
            self.txns.append(txn)
            for i in txn:
                self.itemset.add(frozenset([i]))

    def train(self):
        minsup = len(self.txns) * 0.05
        minconf = 0.5
        largeset = {}
        parents = {}
        rules = {}
        cc = counters = Counter()

        for t in self.txns:
            for item in t:
                counters[frozenset([item])] += 1
        largeset[1] = [k for k,v in counters.items() if v >= minsup]

        k = 1
        while(len(largeset[k])):
            k += 1
            items = largeset[k-1]
            itemset = set(items)
            candidates = set()
            for i in range(len(items)):
                for j in range(i):
                    c = items[i].union(items[j])
                    if c not in candidates and len(c) == k:
                        skip = False
                        for c_1 in it.combinations(c, k-1):
                            if set(c_1) not in itemset:
                                skip = True
                                break
                        if not skip:
                            candidates.add(c)
                            parents[c] = (items[i], items[j])
            for c in candidates:
                counters[c] = 0
                for t in self.txns:
                    if c.issubset(t):
                        counters[c] += 1
            largeset[k] = [c for c in candidates if counters[c] >= minsup]

        print largeset
        for k,v in largeset.items()[2:]:
            for itemset in v:
                lbls = itemset.intersection(self.labels)
                diff = itemset.difference(self.labels)
                if len(diff) and len(lbls):
                    for l in lbls:
                        c1 = cc[itemset]
                        c2 = cc[diff.union(set([l]))]
                        conf = float(c1)/c2
                        if conf > minconf:
                            if diff not in rules or rules[diff][1] <= conf:
                                rules[diff] = (l, conf)
        self.rules = rules
        print self.rules

    def test(self, txn):
        predicted = set()
        print txn.features
        for k,v in self.rules.items():
            if k.issubset(txn.features):
                predicted.add(v[0])
        print 'Predicted: {}, Actual: {}'.format(predicted, txn.labels)

    def evaluate(self, txns):
        return
        np.random.seed(42)
        np.random.shuffle(txns)
        idx = int(len(txns)*0.2)
        for t in txns[0:idx]:
            self.test(t)

