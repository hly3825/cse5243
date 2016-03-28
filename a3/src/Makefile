INPUT='../data/full.txt'

all: knn dtree bayes

knn:
	python main.py -i $(INPUT) -a knn -r 0.95
dtree:
	python main.py -i $(INPUT) -a dtree -r 0.95

bayes: bnb gnb mnb

bnb:
	python main.py -i $(INPUT) -a bnb -r 0.95
gnb:
	python main.py -i $(INPUT) -a gnb -r 0.95
mnb:
	python main.py -i $(INPUT) -a mnb -r 0.95
