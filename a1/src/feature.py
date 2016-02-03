import sys
from sets import Set
from document import Document
from output import *

class Feature:

    def __init__(self, field):
        self.field = field
        self.wordset = Set()
        self.docs = []

    def add(self, doc):
        self.docs.append(doc)
        words = doc.get(self.field)
        for w in words:
            self.wordset.add(w)

    def _print_header(self):
        print 'id',
        for w in self.wordset:
            print str(w),
        print

    def dump(self):
        set_output(self.field)
        self._print_header()
        for d in self.docs:
            words = d.get(self.field)
            print d.id,
            for w in self.wordset:
                print 1 if w in words else 0,
            print
        reset_output()
