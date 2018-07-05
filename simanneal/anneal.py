import csv
import datetime
import logging
import math

import os
import random

logging.basicConfig(format='%(asctime)s - %(filename)s - [line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG)
logging.debug('debug info')
logging.info('info info')
logging.warning('warning info')
logging.error('error info')
logging.critical('critical info')


class Anneal:
    def __init__(self, *args):
        self.problem = args[0]

        self.temperature = args[1]
        self.alpha = args[2]
        self.stopTemperature = args[3]
        self.stopIteration = args[4]
        self.save = args[5]
        self.itertion = 1

        self.currentSolution = self.problem.currentSolution()
        self.bestSolution = self.currentSolution

        self.solutionHistory = [self.currentSolution]

        self.currentCost = self.problem.costFunction(self.currentSolution)
        self.initialCost = self.currentCost
        self.minCost = self.currentCost

        self.costList = [self.currentCost]

        self.acceptHistory = []

    def acceptance_probability(self, candidateCost):
        return math.exp(-abs(candidateCost - self.currentCost) / self.temperature)

    def accept(self, candidate):
        candidateCost = self.problem.costFunction(candidate)

        if candidateCost < self.currentCost:
            acc = ["better solution", "none", "none", "accepted", self.currentSolution, candidate, self.currentCost,
                   candidateCost]

            logging.info("disturb generated a better solution. "
                         " cost function values %s. "
                         " This solution will be accepted immediately." % candidateCost)

            self.currentCost = candidateCost
            self.currentSolution = candidate
            if candidateCost < self.minCost:
                self.minCost = candidateCost
                self.bestSolution = candidate

        else:
            randomGen = random.random()
            acceptance = self.acceptance_probability(candidateCost)
            flag = ("accepted" if randomGen < acceptance else "rejected")
            acc = ["worse solution", randomGen, acceptance, flag, self.currentSolution, candidate, self.currentCost,
                   candidateCost]

            logging.info("disturb generated a worse solution."
                         "cost function values %s" % candidateCost)

            if flag == "accepted":
                self.currentCost = candidateCost
                self.currentSolution = candidate

                logging.info("generated random = %s, acceptance = %s" % (str(randomGen), str(acceptance)))

                logging.info(self.currentSolution)

                logging.info("The new solution was %s" % flag)

        self.acceptHistory.append(acc)

    def anneal(self):
        while self.temperature >= self.stopTemperature and self.itertion < self.stopIteration:
            candidate = self.currentSolution

            logging.info("generation : %d" % self.itertion)
            logging.info("current optimal solution costs: %s" % str(self.currentCost))

            candidate = self.problem.disturb(candidate, self.itertion)

            self.accept(candidate)
            self.temperature *= self.alpha

            self.itertion += 1
            self.costList.append(self.currentCost)
            self.solutionHistory.append(self.currentSolution)

        if self.save:
            self.historySave()

    def historySave(self):
        time = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S')

        path = "history/%s/%s" % (self.problem.__class__.__name__, self.problem.problemName)
        directory = os.path.exists(path)
        if not directory:
            os.makedirs(path)

        filename = ("%s/%s.csv" % (path, time))
        f = open(filename, "w", newline="")
        writer = csv.writer(f)
        for row in self.acceptHistory:
            writer.writerow(row)
        f.close()

        # with open(filename, "w", newline="") as f:
        #     writer = csv.writer(f)
        #     for row in self.acceptHistory:
        #         writer.writerow(row)
