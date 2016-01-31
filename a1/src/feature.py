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

    def dump(self):
        for w in self.wordset:
            print str(w),
        print
        for d in self.docs:
            words = d.get(self.field)
            print d.id,
            for w in self.wordset:
                print 1 if w in words else 0,
            print
