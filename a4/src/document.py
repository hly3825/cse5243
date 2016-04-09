import numpy as np

class document:

    def __init__(self, f):
        self.vectors = []
        f.readline() #ignore header
        for line in f:
            id, lbls, vec = line.translate(None, ',]\n').split('[')
            vec = map(float, vec.split())
            vec = [1 if e > 0 else 0 for e in vec]
            self.vectors.append(vec)

    def jaccard_base(self, a, b):
        return float(len(a & b)) / len(a | b)

    def jaccard_est(self, a, b):
        n = len(a)
        same = sum([1 if a[i]==b[i] else 0 for i in range(n)])
        return float(same) / n

    def get_jaccard_sim(self):
        n = len(self.vectors)
        sets = [0] * n
        print "Number of Documents: ", n
        scores = np.zeros((n, n))
        for i in range(n):
            v = self.vectors[i]
            sets[i] = (set([j for j, e in enumerate(v) if e > 0]))
        for i in range(n):
            for j in range (n):
                scores[i,j] = scores[j,i] = self.jaccard_base(sets[i], sets[j])
        return scores

    def get_sig(self, perms, vec):
        sig = []
        for p in perms:
            v = [vec[i] for i in p]
            sig.append(v.index(1))
        return sig

    def get_minhash(self, k):
        flen = len(self.vectors[0])
        n = len(self.vectors)
        perms = [0] * k
        for i in range(k):
            perms[i] = (np.random.permutation(flen))
        scores = np.zeros((n, n))
        sigs = [self.get_sig(perms, self.vectors[i]) for i in range(n)]
        for i in range(n):
            for j in range (n):
                scores[i,j] = scores[j,i] = self.jaccard_est(sigs[i], sigs[j])
        return scores
