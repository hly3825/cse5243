class document:

    def __init__(self):
        self.labels = {}
        self.vectors = {}

    def build(self, f):
        f.readline() #ignore header
        for line in f:
            id, lbl, vec = line.translate(None, ',]\n').split('[')
            lbl = lbl.split()
            vec = map(float, vec.split())
            vec = [1 if e > 0 else 0 for e in vec]
            self.add_row(id, lbl, vec)

    def add_row(self, id, lbl, vec):
        self.labels[id] = lbl[0]
        self.vectors[id] = vec

    def split(self, ratio=0.8):
        trainx = trainy = test = []
        trainx = self.vectors.values()
        trainy = self.labels.values()
        return trainx, trainy, test
