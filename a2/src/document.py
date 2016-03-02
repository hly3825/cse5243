import numpy as np
from collections import Set
from sklearn.preprocessing import scale
from config import *

class document:

    def __init__(self):
        self.labels = []
        self.vectors = []
        #self.labels = set()

    def build(self, f):
        f.readline() #ignore header
        for line in f:
            id, lbl, vec = line.translate(None, ',]\n').split('[')
            lbl = lbl.split()[0]
            vec = map(float, vec.split())
            self.add_row(lbl, vec)
        self.split_data()

    def add_row(self, lbl, vec):
        self.labels.append(lbl)
        self.vectors.append(vec)
        #self.labels.update(lbl)

    def split_data(self):
        self.data = scale(np.array(self.vectors))
        ntrain = int(self.data.shape[0] * split_ratio)
        np.random.shuffle(self.data)
        self.train = self.data[:ntrain]
        self.test  = self.data[ntrain:]
