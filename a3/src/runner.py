from knn import *
from document import *

class runner:

    def __init__(self):
        #self.options = options().parse()
        self.doc = document()

    def read_input(self):
        #in_file = self.options['input']
        in_file = '../data/mini.txt'
        with open(in_file, 'r') as f:
            self.doc.build(f)

    def run(self):
        self.read_input()
        params = None
        classifier = knn(self.doc, params)
        classifier.evaluate()
