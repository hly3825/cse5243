INPUT='../data/full.txt'

all: knn dtree

knn:
	python main.py -i $(INPUT) -a knn -r 0.95

dtree:
	python main.py -i $(INPUT) -a dtree -r 0.95

bayes:
	python main.py -i $(INPUT) -a bayes -r 0.95
