import sys, getopt
from kmeans import *
from dbscan import *
from agglo  import *
from document import *

class runner:

    def __init__(self):
        self.options = {}
        self.doc = document()
        self.parse_options(sys.argv)

    def read_input(self):
        in_file = self.options['input']
        print "Processing %s" % in_file
        with open(in_file, 'r') as f:
            self.doc.build(f)

    def parse_options(self, args):
        try:
            opts, args = getopt.getopt(args[1:],
                    "i:a:p:h",
                    ["input=", "algo=", "params=", "help"])
        except getopt.GetoptError as err:
            print str(err)
            usage()
            sys.exit(2)

        for o, a in opts:
            if o in ('-i', '--input'):
                self.options['input'] = a
            elif o in ('-a', '--algo'):
                self.options['algo'] = a
            elif o in ('-p', '--params'):
                self.options['params'] = split(a)
            elif o in ('-h', '--help'):
                usage()

    def run(self):
        self.read_input()
        model = kmeans(self.doc)
        model.evaluate()
        #dbs = dbscan(self.doc)
        #dbs.evaluate()
        #agg = agglo(self.doc)
        #agg.evaluate()
