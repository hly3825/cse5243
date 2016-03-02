from sklearn.cluster import DBSCAN
from model import *

class dbscan(model):

    def __init__(self, doc):
        algo = DBSCAN(
                eps=20,
                min_samples=25,
                metric='manhattan')
        model.__init__(self, doc, algo)
