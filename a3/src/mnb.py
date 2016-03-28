from classifier import *
from sklearn.naive_bayes import MultinomialNB

class mnb(classifier):

    def __init__(self, doc):
        algo = MultinomialNB()
        classifier.__init__(self, algo, doc)
