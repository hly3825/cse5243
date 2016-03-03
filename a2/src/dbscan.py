from sklearn.cluster import DBSCAN
from model import *

class dbscan(model):

    def __init__(self, doc, params):
        params = params.split(',')
        epf = float(params[0])
        smp = int(params[1])
        met = params[2]
        algo = DBSCAN(
                eps=epf,
                min_samples=smp,
                metric=met)
        model.__init__(self, doc, algo)
