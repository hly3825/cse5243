class Stopper:

    stopwords = []

    def __init__(self, filename):
        with open(filename, 'r') as sf:
            Stopper.stopwords = sf.read().split()

    def filter(self, text):
        return [word for word in text.split() if word not in Stopper.stopwords]
