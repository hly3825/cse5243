from classifier import *
from sklearn.neighbors import KNeighborsClassifier

class knn(classifier):

    def __init__(self, doc):
        algo = KNeighborsClassifier(n_neighbors=1, algorithm='ball_tree')
        classifier.__init__(self, algo, doc)
