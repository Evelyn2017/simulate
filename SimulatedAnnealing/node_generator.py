import numpy as np

class NodesGenerator:
    def __init__(self, filename):
        self.problem = filename
    '''
    generate nodes
    '''
    def generate(self):
        lines = open(self.problem).readlines()
        x = []
        y = []
        for line in lines[6: len(lines) - 1]:
            params = line.strip().split()
            x.append(params[1])
            y.append(params[2])

        return np.column_stack((np.array(x), np.array(y)))


