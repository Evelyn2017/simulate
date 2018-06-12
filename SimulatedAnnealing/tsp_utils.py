import random
import numpy as np

from SimulatedAnnealing.problem_define import Problem


class TSP(Problem):
    def __init__(self, problem):
        self.problem = problem
        self.coords = self.parseProblem(problem)
        self.distMatrix = self.coordsToDistMatrix(self.coords)

    def parseProblem(self, problem):
        lines = open(problem).readlines()
        x, y = [], []
        for line in lines[6: len(lines) - 1]:
            params = line.strip().split()
            x.append(params[1])
            y.append(params[2])

        return np.column_stack((np.array(x), np.array(y)))

    def costFunction(self, solution):
        return sum([self.distMatrix[i, j] for i, j in zip(solution, solution[1:] + [solution[0]])])

    '''give coords of every city, transfrom these coords to distance matrix'''
    def coordsToDistMatrix(self, coords):
        return np.sqrt((np.square((coords[:, np.newaxis]).astype('float64') - coords.astype('float64')).sum(axis=2)))

    def currentSolution(self):
        node = random.randrange(len(self.distMatrix))
        result = [node]

        nodeToVisit = list(range(len(self.distMatrix)))
        nodeToVisit.remove(node)

        while nodeToVisit:
            nearestNode = min([(self.distMatrix[node][j], j) for j in nodeToVisit], key=lambda x: x[0])
            node = nearestNode[1]
            nodeToVisit.remove(node)
            result.append(node)

        return result



# def vectorToDistMatrix(coords):
#     return np.sqrt((np.square((coords[:, np.newaxis]).astype('float64') - coords.astype('float64')).sum(axis=2)))
#
#
# def nearestNeighbourSolution(dist_matrix):
#     node = random.randrange(len(dist_matrix))
#     result = [node]
#
#     nodes_to_visit = list(range(len(dist_matrix)))
#     nodes_to_visit.remove(node)
#
#     while nodes_to_visit:
#         nearest_node = min([(dist_matrix[node][j], j) for j in nodes_to_visit], key=lambda x: x[0])
#         node = nearest_node[1]
#         nodes_to_visit.remove(node)
#         result.append(node)
#
#     return result
