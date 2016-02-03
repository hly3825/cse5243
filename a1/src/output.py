import sys

class Output:

    def __init__(self, filename):
        self.filename = '../data/output/' + filename + '.txt'

    def _set_output(self):
        print 'Writing to file ' + self.filename
        #sys.stdout = open(self.filename, 'w')

    def _reset_output(self):
        sys.stdout = sys.__stdout__

    def _print_header(self, features):
        print '#id',
        print ' '.join(features),
        print 'places topics'

    def write_data(self, docs, features, matrix):
        self._set_output()
        self._print_header(features)
        for doc in docs:
            print doc.id,
            for f in features:
                print matrix[doc.id][f],
            print doc.places, doc.topics
        self._reset_output()
