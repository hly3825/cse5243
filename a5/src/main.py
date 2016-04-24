import sys, time
import numpy as np
from document import *
from apriori import *

if __name__ == '__main__':
    np.random.seed(42)
    start = time.time()
    f = open(sys.argv[1], 'r')
    doc = document(f)
    apr = apriori(doc.txns)
    apr.train()
    end = time.time()
    print 'Time taken for Training: {}'.format(end - start)
