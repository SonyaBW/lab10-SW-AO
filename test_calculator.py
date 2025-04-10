# https://github.com/SonyaBW/lab10-SW-AO.git
# Partner 1: Sonya Wong
# Partner 2: Ahmad Osman

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(-3, -6), 3)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(0, 1), 0)
        self.assertEqual(multiply(-2, 1), -2)
        self.assertAlmostEqual(multiply(1/3, 3), 1)
        self.assertAlmostEqual(multiply(0.66666666, 5), 3.33333333)
        self.assertAlmostEqual(multiply(1.0, 5), 5.0)

    def test_divide(self): # 3 assertions
        self.assertEqual(divide(0, 1), 0)
        self.assertEqual(divide(-2, 1), -2)
        self.assertAlmostEqual(divide(1 / 3, 3), 1/9)
        self.assertAlmostEqual(divide(0.66666666, 5), 0.13333333)
        self.assertAlmostEqual(divide(1.0, 5), 0.2)
        with self.assertRaises(ZeroDivisionError):
            divide(0.0, 0)
            divide(50, 0)
    # ##########################

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(100, 10), 2)
        self.assertAlmostEqual(logarithm(8, 2), 3)
        self.assertAlmostEqual(logarithm(1, 5), 0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(10, 1)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(1, 0)
            logarithm(2, 0)
            logarithm(5, -10)
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3,4),5)
        self.assertAlmostEqual(hypotenuse(7,12),13.8924439894)
        self.assertAlmostEqual(hypotenuse(4,4),5.65685424949)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(0)
            square_root(-1)
            square_root(-5)
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        self.assertEqual(square_root(9),3)
        self.assertEqual(square_root(25),5)
        self.assertAlmostEqual(square_root(50), 7.07106781187)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()