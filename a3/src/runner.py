from knn import *
from bnb import *
from gnb import *
from mnb import *
from dtree import *
from options import *
from document import *

class runner:

    def __init__(self):
        self.options = options().parse()
        self.doc = document()

    def read_input(self):
        in_file = self.options['input']
        ratio = self.options['ratio']
        with open(in_file, 'r') as f:
            self.doc.build(f, ratio)

    def run(self):
        self.read_input()
        algo = self.options['algo']
        if algo == 'knn':
            classifier = knn(self.doc)
        elif algo == 'dtree':
            classifier = dtree(self.doc)
        elif algo == 'bnb':
            classifier = bnb(self.doc)
        elif algo == 'gnb':
            classifier = gnb(self.doc)
        elif algo == 'mnb':
            classifier = mnb(self.doc)
        classifier.evaluate()
