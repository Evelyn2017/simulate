from abc import ABCMeta, abstractmethod
'''defines each problem'''
class Problem:
    __metaclass__ = ABCMeta

    def __init__(self, problem):
        self.problem = problem

    @abstractmethod
    def costFunction(self):
        pass

    @abstractmethod
    def currentSolution(self):
        pass