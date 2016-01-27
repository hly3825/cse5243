import os
from os.path import join
from bs4 import BeautifulSoup

def process_file(fname):
    s = BeautifulSoup(open(fname), 'lxml')
    for doc in s.findAll('reuters'):
        for e in doc:
            print e

def process_files(input_dir, temp_dir, output_dir, extension):
    print input_dir, temp_dir, output_dir, extension
    for fname in os.listdir(input_dir):
        if fname.endswith(extension):
            process_file(join(input_dir,fname))

if __name__ == '__main__':
    input_dir  = '../data/input'
    temp_dir   = '../data/temp'
    output_dir = '../data/output'
    extension  = '.sgm'

    process_files(input_dir, temp_dir, output_dir, extension)
