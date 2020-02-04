import math


from MathOperations.Addition import Addition
from MathOperations.Subtraction import Subtraction

class Calculator:

    def __init__(self):
        pass

    def addition(self, a, b):
        return Addition.sum(a,b)
    
    def subtraction(self,a,b):
        return Subtraction.difference(a,b)
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