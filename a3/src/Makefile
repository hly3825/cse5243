INPUT='../data/full.txt'
RATIO=0.8

all: knn dtree bayes

knn:
	python main.py -i $(INPUT) -a knn -r $(RATIO)
dtree:
	python main.py -i $(INPUT) -a dtree -r $(RATIO)

bayes: bnb gnb mnb

bnb:
	python main.py -i $(INPUT) -a bnb -r $(RATIO)
gnb:
	python main.py -i $(INPUT) -a gnb -r $(RATIO)
mnb:
	python main.py -i $(INPUT) -a mnb -r $(RATIO)
