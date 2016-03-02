import numpy as np
from collections import Set
from sklearn.preprocessing import scale
from config import *

class document:

    def __init__(self):
        self.labels = []
        self.vectors = []

    def build(self, f):
        f.readline() #ignore header
        for line in f:
            id, lbl, vec = line.translate(None, ',]\n').split('[')
            lbl = lbl.split()
            vec = map(float, vec.split())
            self.add_row(lbl, vec)
        self.data = scale(np.array(self.vectors))

    def add_row(self, lbl, vec):
        self.labels.append(lbl)
        self.vectors.append(vec)
