from stopper import Stopper

def _find_children(doc, parent):
    return [child.string for child in doc.find(parent).find_all('d')]

class Document:
    stopper = Stopper("../data/input/stopwords.txt")

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

    def __str__(self):
        return "{} {}\n{} {}\n{}\n".format(
                self.id, self.date,
                self.topics, self.places,
                self.title)
