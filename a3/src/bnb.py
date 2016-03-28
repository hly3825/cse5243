from classifier import *
from sklearn.naive_bayes import BernoulliNB

class bnb(classifier):

    def __init__(self, doc):
        algo = BernoulliNB()
        classifier.__init__(self, algo, doc)
