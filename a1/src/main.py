import os
from os.path import join
from bs4 import BeautifulSoup

input_dir  = '../data/input'
temp_dir   = '../data/temp'
output_dir = '../data/output'
extension  = '.sgm'
stopfile   = 'stopwords.txt'
stopwords  = []

def read_stopwords():
    global stopwords
    with open(join(input_dir, stopfile), 'r') as sf:
        stopwords = sf.read().split()

def remove_stopwords(text):
    return ' '.join([w for w in text.split() if w not in stopwords])

def find_children(doc, parent):
    for child in doc.find(parent).find_all('d'):
        yield child.string

def process_file(fname):
    print "Processing %s" % fname
    soup = BeautifulSoup(open(fname), 'html.parser')
    for doc in soup.find_all('reuters'):
        id = doc['newid']
        date = doc.find('date').string
        title = doc.find('title').string
        topics = list(find_children(doc, 'topics'))
        places = list(find_children(doc, 'places'))
        body = remove_stopwords(doc.find('body').string.lower())
        print id, date, topics, places
        print remove_stopwords(body)
        print

def process_files():
    print input_dir, temp_dir, output_dir, extension
    for fname in os.listdir(input_dir):
        if fname.endswith(extension):
            process_file(join(input_dir, fname))

if __name__ == '__main__':

    read_stopwords()
    process_files()
