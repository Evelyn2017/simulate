import numpy as np

from simanneal.problem_define.base_problem import Problem


class Constraint(Problem):
    def __init__(self, problem):
        super().__init__(problem)
        self.M0 = 1
        self.C = 4
        self.Mk = self.M0

    def penaltyFactor(self, x):
        g1 = 100 - (x[0] - 5) ** 2 - (x[1] - 5) ** 2
        g2 = -82.81 + (x[0] - 6) ** 2 + (x[1] - 5) ** 2
        g1x = 0 if g1 < 0 else g1
        g2x = 0 if g2 < 0 else g2
        g3x = x[0]
        g4x = x[1]

        return g1x ** 2 + g2x ** 2 + g3x ** 2 + g4x ** 2

    def costFunction(self, x):
        self.Mk *= self.C
        return (x[0] - 10) ** 3 + (x[1] - 20) ** 3 + self.Mk * self.penaltyFactor(x)

    def currentSolution(self):
        x1 = np.random.rand()
        x2 = np.random.rand()
        sol = [12, 3]
        return sol

    def disturb(self, sol, iteration):
        x1 = sol[0] + (2 * np.random.rand() - 1)
        x2 = sol[1] + (2 * np.random.rand() - 1)
        resu = [x1,x2]
        return resu
