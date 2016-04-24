from collections import Counter
from itertools import chain, combinations
from transaction import *

def subsets(arr):
    return chain(*[combinations(arr, i + 1) for i, a in enumerate(arr)])

def joinsets(itemset, length):
    return set([i.union(j) for i in itemset for j in itemset if len(i.union(j)) == length])

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

    def filterbysup(self, itemset):
        minsup = len(self.txns) * 0.05
        self.counters = Counter()
        freqset = Counter()
        for item in itemset:
            for txn in self.txns:
                if item.issubset(txn):
                    freqset[item] += 1
                    self.counters[item] += 1
        return [k for k,v in freqset.items() if v > minsup]

    def genrules(self, largeset):
        self.rules = []
        for i,v in largeset.items()[1:]:
            for itemset in v:
                print itemset, self.counters[itemset]
                diff = itemset.difference(self.labels)
                if(len(diff) > 0):
                    labels = itemset.intersection(self.labels)
                    for l in labels:
                        s1 = self.counters[itemset]
                        s2 = self.counters[diff.union(set[l])]
                        print l, s1

    def train(self):
        largeset = {}
        currset = self.filterbysup(self.itemset)
        k = 2
        while(len(currset)):
            largeset[k-1] = set(currset)
            currset = joinsets(currset, k)
            currset = self.filterbysup(currset)
            k += 1
        self.genrules(largeset)
