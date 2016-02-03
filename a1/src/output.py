import sys

def set_output(filename):
    out_file = '../data/output/' + filename + '.txt'
    print 'Writing to file ' + out_file
    sys.stdout = open(out_file, 'w')

def reset_output():
    sys.stdout = sys.__stdout__
