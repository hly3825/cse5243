import sys, time
import numpy as np
from document import *

def evaluate(base, est):
    mse = np.mean(np.square(base - est))
    rme = np.mean(np.abs(base - est) / (np.maximum(base,
        np.ones(base.shape)*1e-6 )))
    return mse, rme

if __name__ == '__main__':
    np.random.seed(42)
    ks = [16, 32, 64, 128, 256]

    f = open(sys.argv[1], 'r')
    doc = document(f)

    start = time.time()
    base = doc.get_jaccard_sim()
    end = time.time()
    print 'Time taken for Jaccard: {}'.format(end - start)

    for k in ks:
        start = time.time()
        est = doc.get_minhash(k)
        end = time.time()
        mse, rme = evaluate(base, est)
        print 'k: {}, time: {}'.format(k, end - start),
        print ' mse: {}, rme: {}'.format(mse, rme)
