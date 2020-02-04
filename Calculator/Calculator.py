import math


from MathOperations.Addition import Addition
from MathOperations.Subtraction import Subtraction

class Calculator:

    result = 0

    def __init__(self):
        pass

    def addition(self, a, b):
        self.result = Addition.sum(a,b)
        return self.result
    
    def subtraction(self,a,b):
        self.result = Subtraction.difference(a,b)
        return self.result
    '''

    def multiplication(self,a,b):
        return a*b

    def divide(self,a,b):
        return a/b

    def square_root(self,a):
        return math.sqrt(a)

    def square(self,a):
        return a*a

'''