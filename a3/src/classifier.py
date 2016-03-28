import time
from document import *

class classifier:

    def __init__(self, algo, doc):
        self.algo = algo
        self.trainx, self.trainy, self.test = doc.split()

    def eval_training(self):
        start = time.time()
        self.algo.fit(self.trainx, self.trainy)
        end = time.time()
        print 'Training Time: {}'.format(end - start)

    def eval_prediction(self):
        start = time.time()
        predicted = self.algo.predict(self.test)
        end = time.time()
        print 'Testing Time: {}'.format(end - start)

    def evaluate(self):
        self.eval_training()
        #self.eval_prediction()
