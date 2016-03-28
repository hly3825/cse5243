import time
from document import *
from sklearn.metrics import accuracy_score

class classifier:

    def __init__(self, algo, doc):
        self.algo = algo
        self.trainx, self.trainy, self.testx, self.testy = doc.split()

    def eval_training(self):
        start = time.time()
        self.algo.fit(self.trainx, self.trainy)
        end = time.time()
        print 'Training Time: {}'.format(end - start)

    def eval_prediction(self):
        start = time.time()
        predy = self.algo.predict(self.testx)
        end = time.time()
        print 'Testing Time: {}'.format((end - start)/len(predy))
        score = accuracy_score(self.testy, predy, True)
        print 'Accuracy Score: {}'.format(score)

    def evaluate(self):
        self.eval_training()
        self.eval_prediction()
