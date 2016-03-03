from kmeans import *
from dbscan import *
from agglo  import *
from minib  import *
from options import *
from document import *

class runner:

    def __init__(self):
        self.options = options().parse()
        self.doc = document()

    def read_input(self):
        in_file = self.options['input']
        with open(in_file, 'r') as f:
            self.doc.build(f)

    def run(self):
        self.read_input()
        algo = self.options['algo']
        params = self.options['params']
        if algo == 'kmeans':
            model = kmeans(self.doc, params)
        elif algo == 'dbscan':
            model = dbscan(self.doc, params)
        elif algo == 'agglo':
            model = agglo(self.doc, params)
        elif algo == 'minib':
            model = minib(self.doc, params)
        model.evaluate()
