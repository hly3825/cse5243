from sklearn.cluster import KMeans
from model import *

class kmeans(model):

    def __init__(self, doc):
        algo = KMeans(n_clusters=20)
        model.__init__(self, doc, algo)
