import unittest

from Calculator.Calculator import Calculator

class MyTestCase(unittest.TestCase):

    def test_startup(self):
        calculator = Calculator()
        self.assertIsInstance(calculator, Calculator)

    def test_calc_add(self):
        calculator = Calculator()
        result = calculator.addition(1,2)
        self.assertEquals(3,result)

    def test_calc_sub(self):
        calculator = Calculator();
        result = calculator.subtraction(1,2)
        self.assertEquals(-1,result)

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

if __name__ == '__main__':
    unittest.main()