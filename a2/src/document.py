import numpy as np
from collections import Set
from sklearn.preprocessing import scale
from config import *

class document:

    def __init__(self):
        self.ids = []
        self.labels = []
        self.vectors = []
        self.all_labels = set()

    def build(self, f):
        f.readline() #ignore header
        for line in f:
            id, lbl, vec = line.translate(None, ',]\n').split('[')
            lbl = lbl.split()[0]
            vec = map(float, vec.split())
            self.add_row(id, lbl, vec)
        self.split_data()

    def add_row(self, id, lbl, vec):
        self.ids.append(id)
        self.labels.append(lbl)
        self.vectors.append(vec)
        self.all_labels.update(lbl)

    def split_data(self):
        data = scale(np.array(self.vectors))
        ntrain = int(data.shape[0] * split_ratio)
        np.random.shuffle(data)
        self.train = data[:ntrain]
        self.test  = data[ntrain:]
