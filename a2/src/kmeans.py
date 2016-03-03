from sklearn.cluster import KMeans
from model import *

class kmeans(model):

    def __init__(self, doc, params):
        params = params.split(',')
        nc = int(params[0])
        algo = KMeans(n_clusters=nc)
        model.__init__(self, doc, algo)
