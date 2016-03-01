import numpy as np
from collections import Set
from sklearn.cluster import KMeans
from sklearn.preprocessing import scale
from config import *

labels = []
vectors = []
all_labels = set()

def add_row(id, lbl, vec):
    labels.append(lbl)
    vectors.append(vec)
    all_labels.update(l for l in lbl)

def split_data(data,train_split=0.8):
    data = np.array(data)
    num_train = int(data.shape[0] * train_split)
    np.random.shuffle(data)
    return (data[:num_train],data[num_train:])

def read_input(in_file):
    print "Processing %s" % in_file
    with open(in_file, 'r') as f:
        f.readline().split()[2:]
        for line in f:
            id, lbl, vec = line.translate(None, ',]\n').split('[')
            lbl = lbl.split()
            vec = map(float, vec.split())
            add_row(id, lbl, vec)

def process_data(data, nc):
    train, test = split_data(data)
    kmeans = KMeans(n_clusters=nc)
    kmeans.fit(train)
    print kmeans.labels_
    print kmeans.predict(test)


if __name__ == '__main__':
    read_input(in_file)
    process_data(vectors, len(all_labels))
