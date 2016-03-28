from classifier import *
from sklearn.tree import DecisionTreeClassifier

class dtree(classifier):

    def __init__(self, doc):
        algo = DecisionTreeClassifier()
        classifier.__init__(self, algo, doc)
