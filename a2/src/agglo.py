from sklearn.cluster import AgglomerativeClustering
from model import *

class agglo(model):

    def __init__(self, doc, params):
        params = params.split(',')
        nc = int(params[0])
        link = params[1]
        affn = params[2]
        algo = AgglomerativeClustering(
                n_clusters=nc,
                linkage=link,
                affinity=affn)
        model.__init__(self, doc, algo)
