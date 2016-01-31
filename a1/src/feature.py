import sys
from sets import Set
from document import Document

class Feature:

    def __init__(self, field):
        self.field = field
        self.wordset = Set([])
        self.docs = []

    def add(self, doc):
        self.docs.append(doc)
        words = doc.get(self.field)
        for w in words:
            self.wordset.add(w)

    def _set_output(self):
        out_file = '../data/output/' + self.field + '.txt'
        #sys.stdout = open(out_file, 'w')

    def _reset_output(self):
        sys.stdout = sys.__stdout__

    def _print_header(self):
        print 'id',
        for w in self.wordset:
            print str(w),
        print

    def dump(self):
        self._set_output()
        self._print_header()
        for d in self.docs:
            words = d.get(self.field)
            print d.id,
            for w in self.wordset:
                print 1 if w in words else 0,
            print
        self._reset_output()
