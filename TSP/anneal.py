import math
import random
from TSP import visualize_tsp
import matplotlib.pyplot as plt

x_8 = [[0, 1000], [150.9364, 150.9364]]
x_20 = [[0, 1000], [297.0314, 297.0314]]


class SimAnneal(object):
    def __init__(self, coords, T=-1, alpha=0.99, stopping_T=-1, stopping_iter=-1):
        self.coords = coords
        self.N = len(coords)
        self.T = math.sqrt(self.N) if T == -1 else T
        self.alpha = 0.995 if alpha == -1 else alpha
        self.stopping_temperature = 0.00000001 if stopping_T == -1 else stopping_T
        self.stopping_iter = 100000 if stopping_iter == -1 else stopping_iter
        self.iteration = 1

        self.dist_matrix = self.to_dist_matrix(coords)
        self.nodes = [i for i in range(self.N)]

        self.cur_solution = self.initial_solution()
        self.best_solution = list(self.cur_solution)

        self.cur_fitness = self.fitness(self.cur_solution)
        self.initial_fitness = self.cur_fitness
        self.best_fitness = self.cur_fitness

        self.fitness_list = [self.cur_fitness]

    def initial_solution(self):
        """
        最邻近
        """
        cur_node = random.choice(self.nodes)
        solution = [cur_node]

        free_list = list(self.nodes)
        free_list.remove(cur_node)

        while free_list:
            closest_dist = min([self.dist_matrix[cur_node][j] for j in free_list])
            cur_node = self.dist_matrix[cur_node].index(closest_dist)
            free_list.remove(cur_node)
            solution.append(cur_node)

        return solution

    def dist(self, coord1, coord2):
        """
        欧式距离
        """
        return round(math.sqrt(math.pow(coord1[0] - coord2[0], 2) + math.pow(coord1[1] - coord2[1], 2)), 4)

    def to_dist_matrix(self, coords):
        n = len(coords)
        mat = [[self.dist(coords[i], coords[j]) for i in range(n)] for j in range(n)]
        return mat

    def fitness(self, sol):

        return round(sum([self.dist_matrix[sol[i - 1]][sol[i]] for i in range(1, self.N)]) +
                     self.dist_matrix[sol[0]][sol[self.N - 1]], 4)

    def p_accept(self, candidate_fitness):

        return math.exp(-abs(candidate_fitness - self.cur_fitness) / self.T)

    def accept(self, candidate):

        candidate_fitness = self.fitness(candidate)
        if candidate_fitness < self.cur_fitness:
            self.cur_fitness = candidate_fitness
            self.cur_solution = candidate
            if candidate_fitness < self.best_fitness:
                self.best_fitness = candidate_fitness
                self.best_solution = candidate

        else:
            if random.random() < self.p_accept(candidate_fitness):
                self.cur_fitness = candidate_fitness
                self.cur_solution = candidate

    def anneal(self):
        """
        Execute simulated annealing algorithm
        """
        while self.T >= self.stopping_temperature and self.iteration < self.stopping_iter:
            candidate = list(self.cur_solution)
            l = random.randint(2, self.N - 1)
            i = random.randint(0, self.N - l)
            candidate[i:(i + l)] = reversed(candidate[i:(i + l)])
            self.accept(candidate)
            self.T *= self.alpha
            self.iteration += 1

            self.fitness_list.append(self.cur_fitness)

        print('Best fitness obtained: ', self.best_fitness)
        file = open("result.txt", "a")
        file.write(str(self.best_fitness) + "\n")

        print('Improvement over greedy heuristic: ',
              round((self.initial_fitness - self.best_fitness) / (self.initial_fitness), 4))

    def visualize_routes(self):

        visualize_tsp.plotTSP([self.best_solution], self.coords)
        print("best solution", self.best_solution)
        # for i in range(len(self.best_solution)):
        #   print(i, self.best_solution[i])

    def plot_learning(self):
        plt.plot([i for i in range(len(self.fitness_list))], self.fitness_list)
        plt.ylabel('Fitness')
        plt.xlabel('Iteration')
        # plt.plot(x_20[0],x_20[1])
        plt.show()
