import unittest

from MathOperations.Addition import Addition
from MathOperations.Subtraction import Subtraction

class MyTestCase(unittest.TestCase):

    def test_MathOperations_Add(self):
        result = Addition.sum(1,2)
        self.assertEquals(3,result)

    def test_MathOperations_sub(self):
        result = Subtraction.difference(1,2)
        self.assertEquals(-1,result)

    def test_MathOperations_sum_list(self):
        valueList = [1,2,3]
        self.assertEqual(6,Addition.sum(valueList))
'''
    def test_calc_times(self):
        calculator = Calculator();
        result = calculator.multiplication(1,2)
        self.assertEquals(2,result)

    def test_calc_divide(self):
        calculator = Calculator();
        result = calculator.divide(4,2)
        self.assertEquals(2,result)

    def test_calc_sqrt(self):
        calculator = Calculator();
        result = calculator.square_root(9)
        self.assertEquals(3,result)

    def test_calc_squared(self):
        calculator = Calculator();
        result = calculator.square(2)
        self.assertEquals(4,result)
        
        '''

if __name__ == '__main__':
    unittest.main()