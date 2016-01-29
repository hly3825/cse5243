import os,csv
from os.path import join

from bs4 import BeautifulSoup
#from nltk.stem import SnowballStemmer

from document import Document

input_dir  = '../data/input'
temp_dir   = '../data/temp'
output_dir = '../data/output'
extension  = '.sgm'
stopwords  = []
#stemmer    = SnowballStemmer("english")

def process_file(fname):
    print "Processing %s" % fname
    soup = BeautifulSoup(open(fname), 'html.parser')
    for doc in soup.find_all('reuters'):
        d = Document(doc)
        print d

def process_files():
    print input_dir, temp_dir, output_dir, extension
    for fname in os.listdir(input_dir):
        if fname.endswith(extension):
            process_file(join(input_dir, fname))

if __name__ == '__main__':
    process_files()
