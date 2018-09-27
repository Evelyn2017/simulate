import logging

import numpy as np

from simanneal.problem_define.base_problem import Problem


class Constraint(Problem):
    def __init__(self, problem):
        super().__init__(problem)
        self.M0 = 1
        self.C = 4
        self.Mk = self.M0
        self.step = 50

    def penaltyFactor(self, x):
        g1 = 100 - (x[0] - 5) ** 2 - (x[1] - 5) ** 2
        g2 = -82.81 + (x[0] - 6) ** 2 + (x[1] - 5) ** 2
        g1x = 0 if g1 > 0 else g1
        g2x = 0 if g2 > 0 else g2

        return g1x ** 2 + g2x ** 2

    def costFunction(self, x):
        self.Mk *= self.C
        return (x[0] - 10) ** 3 + (x[1] - 20) ** 3 + self.Mk * self.penaltyFactor(x)

    def currentSolution(self):
        x1 = np.random.uniform(13, 100)
        x2 = np.random.uniform(0, 100)
        sol = [x1, x2]
        return sol

    def disturb(self, sol):
        resu = []
        x1 = sol[0] + self.step * (np.random.rand() - 0.5)
        x2 = sol[1] + self.step * (np.random.rand() - 0.5)

        logging.info("generated solution: %s, %s" % (x1, x2))

        self.step *= 0.975

        print(self.step)

        resu = [x1, x2]
        return resu
