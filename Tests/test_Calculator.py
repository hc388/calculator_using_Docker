import unittest

from Calculator.Calculator import Calculator

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_setUp(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calc_return_add(self):
        result = self.calculator.addition(1,2)
        self.assertEqual(3, result)

    def test_calc_return_sub(self):
        result = self.calculator.subtraction(1,2)
        self.assertEqual(-1, result)

    def test_calc_access_sum_result(self):
        self.calculator.addition(1,2)
        self.assertEqual(3, self.calculator.result)

    def test_calc_access_sub_result(self):
        self.calculator.subtraction(1,2)
        self.assertEqual(-1, self.calculator.result)

    def test_multiple_calculators(self):
        calculator1 = Calculator()
        calculator2 = Calculator()

        self.calculator.addition(calculator1.addition(1,2),calculator2.subtraction(3,4))

        self.assertEqual(2, self.calculator3.result)


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