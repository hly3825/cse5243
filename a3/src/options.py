import sys, getopt

class options:

    def __init__(self):
        self.options = {}
        self.options['input'] = './data/full.txt'
        self.options['algo'] = 'knn'
        self.options['ratio'] = 0.8

    def usage(self):
        print "Usage: python main.py [--help] --input=input_file --algo=algorithm --ratio=split_ratio"
        print "input      input file containing the feature vectors"
        print "algo       clustering algorithm to use: knn/bayes/dtree"
        print "ratio      ratio of training data : test data"
        print

    def parse(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:],
                    "i:a:r:h",
                    ["input=", "algo=", "ratio=", "help"])
        except getopt.GetoptError as err:
            print str(err)
            self.usage()
            sys.exit(2)

        for o, a in opts:
            if o in ('-i', '--input'):
                self.options['input'] = a
            elif o in ('-a', '--algo'):
                self.options['algo'] = a
            elif o in ('-r', '--ratio'):
                self.options['ratio'] = float(a)
            elif o in ('-h', '--help'):
                self.usage()
                sys.exit(0)

        print 'input: {}, algo: {}, ratio: {}'.format(
                self.options['input'],
                self.options['algo'],
                self.options['ratio'])
        return self.options
