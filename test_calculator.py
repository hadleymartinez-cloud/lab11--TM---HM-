import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 3), 2)

    ######## Partner 1
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)

    def test_logarithm(self):
        self.assertEqual(calculator.logarithm(10, 100), 2)

    ######## Partner 2
   def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)

   
    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)
          
    def test_multiply(self):
        self.assertEqual(calculator.mul(3, 4), 12)

    def test_divide(self):
        self.assertEqual(calculator.div(2, 10), 5)

    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(10, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(9), 3)
        with self.assertRaises(ValueError):
            calculator.square_root(-1)


if __name__ == '__main__':
    unittest.main()
# Do not touch this
if __name__ == "__main__":
    unittest.main()
