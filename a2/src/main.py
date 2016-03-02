import numpy as np
from collections import Counter
from config import *
from kmeans import *
from dbscan import *
from agglo  import *
from document import *

def read_input(in_file):
    d = document();
    print "Processing %s" % in_file
    with open(in_file, 'r') as f:
        d.build(f)
    return d

if __name__ == '__main__':
    np.random.seed(42)
    d = read_input(in_file)
    kmn = kmeans(d)
    kmn.evaluate()
    dbs = dbscan(d)
    dbs.evaluate()
    agg = agglo(d)
    agg.evaluate()
