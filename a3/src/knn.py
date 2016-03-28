from classifier import *
from sklearn.neighbors import KNeighborsClassifier

class knn(classifier):

    def __init__(self, doc):
        algo = KNeighborsClassifier()
        classifier.__init__(self, algo, doc)
