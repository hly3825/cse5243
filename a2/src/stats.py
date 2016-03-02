import numpy as np
from collections import Counter
from scipy.stats import entropy

def get_entropy(clusters):
    return entropy(Counter(clusters).values())

def get_variance(clusters):
    return np.var(Counter(clusters).values())


