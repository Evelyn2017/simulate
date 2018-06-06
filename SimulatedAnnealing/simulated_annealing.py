import math
import random
import matplotlib.pyplot as plt

import SimulatedAnnealing.tsp_utils as tsp_utils


class SimulatedAnnealing:
    def __init__(self, coords, temp, alpha, stopping_temp, stopping_iter):

        self.coords = coords
        self.sample_size = len(coords)
        self.temp = temp
        self.alpha = alpha
        self.stopping_temp = stopping_temp
        self.stopping_iter = stopping_iter
        self.iteration = 1

        self.dist_matrix = tsp_utils.vectorToDistMatrix(coords)
        self.curr_solution = tsp_utils.nearestNeighbourSolution(self.dist_matrix)
        self.best_solution = self.curr_solution

        self.solution_history = [self.curr_solution]

        self.curr_weight = self.weight(self.curr_solution)
        self.initial_weight = self.curr_weight
        self.min_weight = self.curr_weight

        self.weight_list = [self.curr_weight]

        print('Intial weight: ', self.curr_weight)

    def weight(self, sol):
        return sum([self.dist_matrix[i, j] for i, j in zip(sol, sol[1:] + [sol[0]])])

    def acceptance_probability(self, candidate_weight):

        return math.exp(-abs(candidate_weight - self.curr_weight) / self.temp)

    def accept(self, candidate):

        candidate_weight = self.weight(candidate)
        if candidate_weight < self.curr_weight:
            self.curr_weight = candidate_weight
            self.curr_solution = candidate
            if candidate_weight < self.min_weight:
                self.min_weight = candidate_weight
                self.best_solution = candidate

        else:
            if random.random() < self.acceptance_probability(candidate_weight):
                self.curr_weight = candidate_weight
                self.curr_solution = candidate

    def anneal(self):

        while self.temp >= self.stopping_temp and self.iteration < self.stopping_iter:
            candidate = list(self.curr_solution)
            l = random.randint(2, self.sample_size - 1)
            i = random.randint(0, self.sample_size - l)

            candidate[i: (i + l)] = reversed(candidate[i: (i + l)])

            self.accept(candidate)
            self.temp *= self.alpha
            self.iteration += 1
            self.weight_list.append(self.curr_weight)
            self.solution_history.append(self.curr_solution)

        print('Sample size: ', self.sample_size)
        print('Minimum weight: ', self.min_weight)
        print('Improvement: ',
              round((self.initial_weight - self.min_weight) / (self.initial_weight), 4) * 100, '%')

    def optimizedPrint(self):
        xs = []
        ys = []

        for i in self.best_solution:
            xs.append(int(self.coords[i][0]))
            ys.append(int(self.coords[i][1]))

        plt.title("Optimized weight: %s" % self.min_weight)

        plt.plot(xs, ys, marker=".", color="black")
        plt.plot(xs[0], ys[0], marker="*", color="red")
        plt.plot(xs[-1], ys[-1], marker="*", color="green")
        plt.show()

    def plotLearning(self):
        plt.plot([i for i in range(len(self.weight_list))], self.weight_list)

        line_init = plt.axhline(y=self.initial_weight, color='r', linestyle='--')
        line_min = plt.axhline(y=self.min_weight, color='g', linestyle='--')
        line_right = plt.axhline(y = 426, color = "purple", linestyle = "--")
        plt.legend([line_init, line_min, line_right], ['Initial weight', 'Optimized weight', 'standard_weight'])
        plt.ylabel('Weight')
        plt.xlabel('Iteration')
        plt.annotate("%s" % self.min_weight, xy=(0, self.min_weight))
        plt.show()
