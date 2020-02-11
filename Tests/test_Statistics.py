import unittest

from Statistics.Statistics import Statistics
import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_Statistics_Mean(self):
        data = [10,20,30,40,50]
        self.assertEquals(30,Statistics.mean(self,data))



if __name__ == '__main__':
    unittest.main()
