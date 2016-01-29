import os,csv
from os.path import join

from bs4 import BeautifulSoup
#from nltk.stem import SnowballStemmer

from document import Document

input_dir  = '../data/input'
temp_dir   = '../data/temp'
output_dir = '../data/output'
extension  = '.sgm'
stopfile   = 'stopwords.txt'
stopwords  = []
#stemmer    = SnowballStemmer("english")

def read_stopwords():
    global stopwords
    with open(join(input_dir, stopfile), 'r') as sf:
        stopwords = sf.read().split()

def join_words(words):
    return ' '.join(words)

def remove_stopwords(text):
    return [word for word in text.split() if word not in stopwords]

def find_children(doc, parent):
    return [child.string for child in doc.find(parent).find_all('d')]

def process_file(fname):
    print "Processing %s" % fname
    soup = BeautifulSoup(open(fname), 'html.parser')
    for doc in soup.find_all('reuters'):
        id = doc['newid']
        date = doc.find('date').string
        title = doc.find('title').string
        topics = find_children(doc, 'topics')
        places = find_children(doc, 'places')
        body = remove_stopwords(doc.find('body').string.lower())
        #body = map(stemmer.stem, body)
        d = Document(id, date, title, topics, places, body)
        print d

def process_files():
    print input_dir, temp_dir, output_dir, extension
    for fname in os.listdir(input_dir):
        if fname.endswith(extension):
            process_file(join(input_dir, fname))

if __name__ == '__main__':

    read_stopwords()
    process_files()
