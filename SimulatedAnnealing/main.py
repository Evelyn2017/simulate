# from nodes_generator import NodeGenerator
# from simulated_annealing import SimulatedAnnealing
import datetime

from SimulatedAnnealing.node_generator import NodesGenerator
from SimulatedAnnealing.simulated_annealing import SimulatedAnnealing


def main():

    temperature = 10
    stopTemperature = 0.001
    alpha = 0.9999
    stopIteration = 50000


    problem = "problems/eil51.txt"

    nodes = NodesGenerator(problem).generate()

    sa = SimulatedAnnealing(nodes, temperature, alpha, stopTemperature, stopIteration)
    sa.anneal()

    print("Best solution: " + str(sa.best_solution))

    sa.optimizedPrint()

    sa.plotLearning()


if __name__ == "__main__":
    start = datetime.datetime.now()
    main()
    end = datetime.datetime.now()
    print("time: " + str(end - start))
