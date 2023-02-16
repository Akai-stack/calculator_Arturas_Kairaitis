import unittest
from calculator import Calculator, perform_operation


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2), 2)
        self.assertEqual(self.calc.add(3), 5)
        self.assertEqual(self.calc.add(-5), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2), -2)
        self.assertEqual(self.calc.subtract(3), -5)
        self.assertEqual(self.calc.subtract(-5), 0)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2), 0)
        self.assertEqual(self.calc.multiply(3), 0)
        self.assertEqual(self.calc.multiply(-5), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(2), 0)
        self.assertEqual(self.calc.divide(3), 0)
        self.assertEqual(self.calc.divide(-5), 0)

    def test_reset(self):
        self.assertEqual(self.calc.reset(), 0)

    def test_n_root(self):
        self.assertEqual(self.calc.n_root(4), 2)
        self.assertEqual(self.calc.n_root(9), 3)

    def test_perform_operation(self):
        self.assertEqual(perform_operation(self.calc, "add", 2), 2)
        self.assertEqual(perform_operation(self.calc, "subtract", 1), 1)
        self.assertEqual(perform_operation(self.calc, "multiply", 3), 0)
        self.assertEqual(perform_operation(self.calc, "divide", 2), 0)
        self.assertEqual(perform_operation(self.calc, "reset"), 0)
        self.assertEqual(perform_operation(self.calc, "n_root", 4), 2)
        self.assertEqual(perform_operation(self.calc, "invalid"), "Invalid Operation")


if __name__ == '__main__':
    unittest.main()
