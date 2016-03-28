from classifier import *
from sklearn.neighbors import KNeighborsClassifier

class knn(classifier):

    def __init__(self, doc, params):
        #params = params.split(',')
        algo = KNeighborsClassifier()
        classifier.__init__(self, algo, doc)
