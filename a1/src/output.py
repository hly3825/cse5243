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
        print '#topics',
        print ' '.join(features)

    def write_data(self, docs, features, matrix):
        self._set_output()
        self._print_header(features)
        for doc in docs:
            vector = [matrix[doc.id].get(f, 0) for f in features]
            if not all(v == 0 for v in vector):
                print doc.id, doc.topics, vector
        self._reset_output()
