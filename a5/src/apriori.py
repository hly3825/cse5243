from collections import Counter
from transaction import *

class apriori:

    def __init__(self, txns):
        self.txns = []
        self.itemset = set()
        for t in txns:
            txn = frozenset(t.features+t.labels)
            self.txns.append(txn)
            for i in txn:
                self.itemset.add(frozenset([i]))

    def filterbysup(self, itemset):
        minsup = len(self.txns) * 0.15
        self.counters = Counter()
        freqset = Counter()
        for item in itemset:
            for txn in self.txns:
                if item.issubset(txn):
                    freqset[item] += 1
                    self.counters[item] += 1
        return [k for k,v in freqset.items() if v > minsup]

    def subsets(self, itemset, length):
        return set([i.union(j) for i in itemset for j in itemset if len(i.union(j)) == length])

    def train(self):
        largeset = {}
        currset = self.filterbysup(self.itemset)
        k = 2
        while(len(currset)):
            largeset[k-1] = currset
            currset = self.subsets(currset, k)
            currset = self.filterbysup(currset)
            k += 1

        print self.counters
