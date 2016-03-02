import sys, getopt

class options:

    def __init__(self):
        self.options = {}

    def usage(self):
        print "Usage: python main.py [--help] --input=input_file --algo=algorithm --params=extra_params"
        print
        print "input      input file containing the feature vectors"
        print "algo       clustering algorithm to use: kmeans, dbscan, agglo"
        print "params     extra parameters to be passed to the algorithm"
        print

    def parse(self):
        try:
            opts, args = getopt.getopt(sys.argv[1:],
                    "i:a:p:h",
                    ["input=", "algo=", "params=", "help"])
        except getopt.GetoptError as err:
            print str(err)
            self.usage()
            sys.exit(2)

        for o, a in opts:
            if o in ('-i', '--input'):
                self.options['input'] = a
            elif o in ('-a', '--algo'):
                self.options['algo'] = a
            elif o in ('-p', '--params'):
                self.options['params'] = split(a)
            elif o in ('-h', '--help'):
                self.usage()

        return self.options
