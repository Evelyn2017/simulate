from abc import ABCMeta, abstractmethod
'''abstract class :
   defines each problem'''
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
    def generateNewSolution(self, *args):
        pass