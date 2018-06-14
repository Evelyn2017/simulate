from simanneal.anneal import Anneal
from simanneal.problem_define.tsp_utils import TSP
from simanneal.visualize import annealPlot


def main():
    """The algorithm requires a problem define
    and known optimal solution to the problem"""

    # problem = Function("function", -1549)
    problem = TSP("data/eil51.csv", 426)

    temperature = 10
    stopTemperature = 0.001
    alpha = 0.9999
    stopIteration = 30

    '''save history data in files. boolean. default = False'''
    save = True

    params = [problem, temperature, alpha, stopTemperature, stopIteration]

    sa = Anneal(params[0], params[1], params[2], params[3], params[4], save)
    sa.anneal()

    annealPlot(sa)

    # sa.historySave()
    # detailPlot(sa, 30)


if __name__ == "__main__":
    main()
