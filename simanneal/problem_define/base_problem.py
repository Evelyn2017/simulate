from abc import ABCMeta, abstractmethod

'''
This abstract class defines an outline of every specific problem which includes:
    __init__():data of one problem,
    costFunction():cost function for simulated annealing,
    currentSolution():generate a solution,
    disturb():disturb current solution to generate a new solution. 
'''


class Problem:
    __metaclass__ = ABCMeta

    def __init__(self, problem):
        self.problem = problem

    @abstractmethod
    def costFunction(self, *args):
        pass

    @abstractmethod
    def currentSolution(self):
        pass

    '''disturb to generate a new solution based on a candidate'''

    @abstractmethod
    def disturb(self, *args):
        pass
