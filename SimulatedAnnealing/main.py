# from nodes_generator import NodeGenerator
# from simulated_annealing import SimulatedAnnealing
import datetime

from SimulatedAnnealing.node_generator import NodesGenerator
from SimulatedAnnealing.simulated_annealing import SimulatedAnnealing


def main():
    temp = 10
    stopping_temp = 0.001
    alpha = 0.9999
    stopping_iter = 50000

    problem = "problems/eil51.txt"

    nodes = NodesGenerator(problem).generate()

    sa = SimulatedAnnealing(nodes, temp, alpha, stopping_temp, stopping_iter)
    sa.anneal()

    print("Best solution: " + str(sa.best_solution))

    sa.optimizedPrint()

    sa.plotLearning()


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    print("time: " + str(end - start))
