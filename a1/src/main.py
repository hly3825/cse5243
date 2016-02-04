import os
from os.path import join
from bs4 import BeautifulSoup
from document import Document
from feature import *
from config import *

f  = Feature()

def process_file(fname):
    print "Processing %s" % fname
    soup = BeautifulSoup(open(fname), 'html.parser')
    for doc in soup.find_all('reuters'):
        try:
            d = Document(doc)
            f.add(d)
        except Exception as e:
            #print e.message
            pass

def process_files():
    for fname in os.listdir(input_dir):
        if fname.endswith(extension):
            process_file(join(input_dir, fname))

if __name__ == '__main__':
    process_files()
    f.build()
    f1 = Feature1(f)
    f1.write()
    f2 = Feature2(f)
    f2.write()
