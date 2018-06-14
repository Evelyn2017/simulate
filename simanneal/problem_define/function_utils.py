import numpy as np

from simanneal.problem_define.base_problem import Problem


class Function(Problem):
    def __init__(self,problem, standardCost):
        super().__init__(problem)
        self.standardCost = standardCost

    def costFunction(self, x):
        return (x - 2) * (x + 3) * (x + 8) * (x - 9)

    def currentSolution(self):
        return 10 * (2 * np.random.rand() - 1)

    def disturb(self, *args):
        return self.currentSolution() + (2 * np.random.rand() - 1)
