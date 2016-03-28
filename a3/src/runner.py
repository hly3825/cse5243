from knn import *
from dtree import *
from bayes import *
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
        elif algo == 'bayes':
            classifier = bayes(self.doc)
        classifier.evaluate()
