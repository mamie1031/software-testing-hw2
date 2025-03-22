import unittest
from calculator import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5

    def test_substract(self):
        calc = Calculator()
        result = calc.substract(2, 3)
        self.assertEqual(result, -1)

    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(2, 3)
        self.assertEqual(result, 6)
    def test_divide(self):
        calc = Calculator()
        result = calc.divide(10, 2)
        self.assertEqual(result, 5)
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == "__main__":
    unittest.main()