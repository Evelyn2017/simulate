# from nodes_generator import NodeGenerator
# from simulated_annealing import SimulatedAnnealing
from commonSimulate.nodes_generator import NodeGenerator
from commonSimulate.simulated_annealing import SimulatedAnnealing


def main():
    temp = 1000
    stopping_temp = 0.00000001
    alpha = 0.9995
    stopping_iter = 10000000

    size_width = 20
    size_height = 20

    population_size = 20

    nodes = NodeGenerator(size_width, size_height, population_size).generate()


    sa = SimulatedAnnealing(nodes, temp, alpha, stopping_temp, stopping_iter)
    sa.anneal()

    sa.animateSolutions()

    print(sa.best_solution)
    sa.plotLearning()


if __name__ == "__main__":
    main()