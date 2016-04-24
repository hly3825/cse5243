from transaction import *
import numpy as np

class document:

    def __init__(self, f):
        self.txns = []
        f.readline() #ignore header
        for line in f:
            id, lbls, vec = line.translate(None, ',]\n').split('[')
            lbls = lbls.split()
            vec = map(float, vec.split())
            vec = [i for i, e in enumerate(vec) if e > 0]
            t = transaction(id, lbls, vec)
            self.txns.append(t)
