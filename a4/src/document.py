import numpy as np
from sklearn.metrics import jaccard_similarity_score

class document:

    def __init__(self, f):
        self.vectors = []
        f.readline() #ignore header
        for line in f:
            id, lbls, vec = line.translate(None, ',]\n').split('[')
            vec = map(float, vec.split())
            vec = [1 if e > 0 else 0 for e in vec]
            self.vectors.append(vec)

    def get_jaccard_sim(self):
        n = len(self.vectors)
        print "Number of Documents: ", n
        scores = np.zeros((n, n))
        for i in range(n):
            for j in range (n):
                scores[i,j] = scores[j,i] = jaccard_similarity_score(self.vectors[i], self.vectors[j])
        return scores

    def get_sig(self, vec):
        sig = []
        for p in self.perms:
            v = [vec[i] for i in p]
            sig.append(v.index(1))
        return sig

    def get_minhash(self, k):
        flen = len(self.vectors[0])
        self.perms = [0] * k
        for i in range(k):
            self.perms[i] = np.random.permutation(flen)
        n = len(self.vectors)
        scores = np.zeros((n, n))
        sigs = [self.get_sig(self.vectors[i]) for i in range(n)]
        for i in range(n):
            for j in range (n):
                scores[i,j] = scores[j,i] = jaccard_similarity_score(sigs[i], sigs[j])
        return scores
