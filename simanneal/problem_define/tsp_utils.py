"""This class defines TSP problems."""

import numpy as np
import random

from simanneal.problem_define.base_problem import Problem


class TSP(Problem):
    def __init__(self, problem, standardCost):
        super().__init__(problem)

        self.standardCost = standardCost

        self.coords = self.parseProblem(problem)
        self.distMatrix = self.coordsToDistMatrix(self.coords)
        self.sampleSize = len(self.coords)

        self.problemName = problem[5:-4]

    def parseProblem(self, problem):
        lines = open(problem).readlines()
        x, y = [], []
        for line in lines[0: len(lines)]:
            params = line.strip().split(",")
            x.append(params[1])
            y.append(params[2])

        return np.column_stack((np.array(x), np.array(y)))

    def coordsToDistMatrix(self, coords):
        return np.sqrt((np.square((coords[:, np.newaxis]).astype('float64') - coords.astype('float64')).sum(axis=2)))

    def costFunction(self, solution):
        return sum([self.distMatrix[i, j] for i, j in zip(solution, solution[1:] + [solution[0]])])

    '''give coords of every city, transform these coords into distance matrix'''

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

    '''disturb to generate a new solution based on current solution
        reverse solution sequence'''

    def disturb(self, solution):
        solution = list(solution)
        l = random.randint(2, self.sampleSize - 1)
        i = random.randint(0, self.sampleSize - l)
        solution[i: (i + l)] = reversed(solution[i: (i + l)])

        return solution
