import os
from os.path import join

from bs4 import BeautifulSoup

from document import Document
from tfidf import Tfidf
from feature import Feature

input_dir  = '../data/input/test'
extension  = '.sgm'
tfidf      = Tfidf()
topics     = Feature('topics')
places     = Feature('places')

def process_file(fname):
    print "Processing %s" % fname
    soup = BeautifulSoup(open(fname), 'html.parser')
    for doc in soup.find_all('reuters'):
        try:
            d = Document(doc)
            tfidf.add(d)
            topics.add(d)
            places.add(d)
        except:
            pass

def process_files():
    for fname in os.listdir(input_dir):
        if fname.endswith(extension):
            process_file(join(input_dir, fname))

if __name__ == '__main__':
    process_files()
    tfidf.dump()
    topics.dump()
    places.dump()
