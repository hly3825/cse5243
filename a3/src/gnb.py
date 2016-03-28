from classifier import *
from sklearn.naive_bayes import GaussianNB

class gnb(classifier):

    def __init__(self, doc):
        algo = GaussianNB()
        classifier.__init__(self, algo, doc)
