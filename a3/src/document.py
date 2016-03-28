import random
from sklearn import preprocessing

class document:

    def __init__(self):
        self.labels = []
        self.vectors = []

    def build(self, f, r):
        f.readline() #ignore header
        for line in f:
            id, lbls, vec = line.translate(None, ',]\n').split('[')
            lbls = lbls.split()
            vec = map(float, vec.split())
            #vec = [1 if e > 0 else 0 for e in vec]
            self.add_row(lbls, vec)
        self.transform_labels()
        self.ratio = r

    def add_row(self, lbls, vec):
        for lbl in lbls:
            self.labels.append(lbl)
            self.vectors.append(vec)

    def transform_labels(self):
        le = preprocessing.LabelEncoder()
        le.fit(self.labels)
        self.labels = le.transform(self.labels)

    def split(self):
        rows = zip(self.vectors, self.labels)
        random.shuffle(rows)
        self.vectors[:], self.labels[:] = zip(*rows)
        idx = int(len(rows)*self.ratio)
        trainx = self.vectors[:idx]
        trainy = self.labels[:idx]
        testx = self.vectors[idx:]
        testy = self.labels[idx:]
        return trainx, trainy, testx, testy
