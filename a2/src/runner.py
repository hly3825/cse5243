from kmeans import *
from dbscan import *
from agglo  import *
from options import *
from document import *

class runner:

    def __init__(self):
        self.options = options().parse()
        self.doc = document()

    def read_input(self):
        in_file = self.options['input']
        print "Processing %s" % in_file
        with open(in_file, 'r') as f:
            self.doc.build(f)

    def run(self):
        self.read_input()
        model = kmeans(self.doc)
        model.evaluate()
        #dbs = dbscan(self.doc)
        #dbs.evaluate()
        #agg = agglo(self.doc)
        #agg.evaluate()
