from classifier import *
from sklearn.naive_bayes import GaussianNB

class bayes(classifier):

    def __init__(self, doc):
        algo = GaussianNB()
        classifier.__init__(self, algo, doc)
