import sys
from config import *

class Output:

    def __init__(self, filename):
        self.filename = output_dir + filename + '.txt'

    def _set_output(self):
        print 'Writing to file ' + self.filename
        sys.stdout = open(self.filename, 'w')

    def _reset_output(self):
        sys.stdout = sys.__stdout__

    def _print_header(self, features):
        print '#id',
        print ' '.join(features)

    def write_data(self, docs, features, matrix):
        self._set_output()
        self._print_header(features)
        for doc in docs:
            print doc.id,
            for f in features:
                print matrix[doc.id].get(f, 0),
            print
        self._reset_output()
