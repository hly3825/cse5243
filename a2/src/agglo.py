from sklearn.cluster import AgglomerativeClustering
from model import *

class agglo(model):

    def __init__(self, doc):
        algo = AgglomerativeClustering(
                n_clusters=20,
                linkage='average',
                affinity='manhattan')
        model.__init__(self, doc, algo)
