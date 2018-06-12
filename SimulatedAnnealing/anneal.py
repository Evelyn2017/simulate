import math
import random
import matplotlib.pyplot as plt

import SimulatedAnnealing.tsp_utils as tsp_utils
from SimulatedAnnealing.problem_define import Problem
from SimulatedAnnealing.tsp_utils import TSP


class Anneal:
    def __init__(self, problem, temperature, alpha, stopTemperature, stopIteration):
        self.problem = Problem(problem)

        self.temperature = temperature
        self.alpha = alpha
        self.stopTemperature = stopTemperature
        self.stopIteration = stopIteration

        self.currentSolution = self.problem.currentSolution()
        self.bestSolution = self.currentSolution

        self.solutionHistory = [self.currentSolution]

        self.currentCost = self.problem.costFunction()
        self.initialCost = self.currentCost
        self.minCost = self.currentCost

        self.costList = [self.currentCost]

    def acceptance_probability(self, candidateCost):
        return math.exp(-abs(candidateCost - self.currentCost) / self.temperature)

    def accept(self, candidate):
        candidateCost = self.currentCost
        if candidateCost < self.currentCost:
            self.currentCost = candidateCost
            self.currentSolution = candidate
            if candidateCost < self.minCost:
                self.minCost = candidateCost
                self.bestSolution = candidate

        else:
            if random.random() < self.acceptance_probability(candidateCost):
                self.currentCost = candidateCost
                self.currentSolution = candidate

    def anneal(self):
        pass

problem = TSP("problems/eil51.txt")
sa = Anneal(problem, 10, 0.9999, 0.01, 50000)
print(sa.problem.__class__)