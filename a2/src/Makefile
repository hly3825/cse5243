INPUT='./data/mini2.txt'

all: kmeans dbscan agglo minibatch

kmeans:
	python main.py -i $(INPUT) -a kmeans -p 4
	python main.py -i $(INPUT) -a kmeans -p 8
	python main.py -i $(INPUT) -a kmeans -p 12
	python main.py -i $(INPUT) -a kmeans -p 20

dbscan:
	python main.py -i $(INPUT) -a dbscan -p 0.5,5,euclidean
	python main.py -i $(INPUT) -a dbscan -p 0.5,5,manhattan
	python main.py -i $(INPUT) -a dbscan -p 1,10,euclidean
	python main.py -i $(INPUT) -a dbscan -p 1,10,manhattan

agglo:
	python main.py -i $(INPUT) -a agglo -p 10,ward,euclidean
	python main.py -i $(INPUT) -a agglo -p 10,average,cosine
	python main.py -i $(INPUT) -a agglo -p 10,average,euclidean
	python main.py -i $(INPUT) -a agglo -p 10,average,manhattan

minibatch:
	python main.py -i $(INPUT) -a minib -p 10,10
	python main.py -i $(INPUT) -a minib -p 10,25
	python main.py -i $(INPUT) -a minib -p 10,100
	python main.py -i $(INPUT) -a minib -p 20,20
