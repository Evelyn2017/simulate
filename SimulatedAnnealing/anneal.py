import math
import random
import matplotlib.pyplot as plt

import SimulatedAnnealing.tsp_utils as tsp_utils
from SimulatedAnnealing.problem_define import Problem
from SimulatedAnnealing.tsp_utils import TSP


class Anneal:
    def __init__(self, problem, temperature, alpha, stopTemperature, stopIteration):
        self.problem = problem

        self.temperature = temperature
        self.alpha = alpha
        self.stopTemperature = stopTemperature
        self.stopIteration = stopIteration
        self.itertion = 1

        self.currentSolution = self.problem.currentSolution()
        self.bestSolution = self.currentSolution

        self.solutionHistory = [self.currentSolution]

        self.currentCost = self.problem.costFunction(self.currentSolution)
        self.initialCost = self.currentCost
        self.minCost = self.currentCost

        self.costList = [self.currentCost]

        self.acc = []

    def acceptance_probability(self, candidateCost):
        return math.exp(-abs(candidateCost - self.currentCost) / self.temperature)

    def accept(self, candidate):
        candidateCost = self.problem.costFunction(candidate)
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
        while self.temperature >= self.stopTemperature and self.itertion < self.stopIteration:
            candidate = list(self.currentSolution)
            l = random.randint(2, self.problem.sampleSize - 1)
            i = random.randint(0, self.problem.sampleSize - l)

            candidate[i: (i + l)] = reversed(candidate[i: (i + l)])

            self.accept(candidate)
            self.temperature *= self.alpha
            self.itertion += 1
            self.costList.append(self.currentCost)
            self.solutionHistory.append(self.currentSolution)

    def plotLearning(self):
        plt.plot([i for i in range(len(self.costList))], self.costList)

        line_init = plt.axhline(y=self.initialCost, color='r', linestyle='--')
        line_min = plt.axhline(y=self.minCost, color='g', linestyle='--')
        line_right = plt.axhline(y=426, color="purple", linestyle="--")
        plt.legend([line_init, line_min, line_right], ['Initial weight', 'Optimized weight', 'standard_weight'])
        plt.ylabel('Weight')
        plt.xlabel('Iteration')
        plt.annotate("%s" % self.minCost, xy=(0, self.minCost))
        print(self.costList)
        plt.show()

