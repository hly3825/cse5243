from stopper import Stopper
#from nltk.stem import SnowballStemmer

def _find_children(doc, parent):
    return [child.string for child in doc.find(parent).find_all('d')]

class Document:
    stopper = Stopper("../data/input/stopwords.txt")
    #stemmer = SnowballStemmer("english")

    def __init__(self, doc):
        self.id = doc['newid']
        self.date = doc.find('date').string
        self.topics = _find_children(doc, 'topics')
        self.places = _find_children(doc, 'places')
        title = doc.find('title').string.lower()
        title = Document.stopper.filter(title)
        self.title = title
        body = doc.find('body').string.lower()
        body = Document.stopper.filter(body)
        #body = map(stemmer.stem, body)
        self.body = body

    def get(self, field):
        return self.__dict__[field]
