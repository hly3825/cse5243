import sys, time
from document import *
from apriori import *

if __name__ == '__main__':
    start = time.time()
    f = open(sys.argv[1], 'r')
    doc = document(f)
    apr = apriori(doc.txns)
    apr.train()
    end = time.time()
    print 'Time taken for Training: {}'.format(end - start)

    start = time.time()
    apr.evaluate(doc.txns)
    end = time.time()
    print 'Time taken for Testing: {}'.format(end - start)
