# tests/calculator/test_factorize.py
import unittest
from src.calculator import Calculator

class TestCalculatorFactorize(unittest.TestCase):
    def setUp(self):
        # Obtain a singleton instance of Calculator for all tests
        self.calc = Calculator()

    def test_regular_cases(self):
        """Test factorize on regular inputs."""
        test_cases = [
            (1, []),
            (2, [2]),
            (3, [3]),
            (4, [2, 2]),
            (27, [3, 3, 3]),
            (65536, [2] * 16),
            (10952347, [7, 23, 59, 1153]),
            (100000039, [100000039]),
        ]
        for n, expected in test_cases:
            with self.subTest(n=n):
                self.assertEqual(self.calc.factorize(n), expected)

    def test_corner_cases(self):
        """Test factorize on boundary inputs."""
        # Factorization of 0 is treated as an empty list
        self.assertEqual(self.calc.factorize(0), [])
        # Max int – 1
        self.assertEqual(
            self.calc.factorize(2147483646),
            [2, 3, 3, 7, 11, 31, 151, 331],
        )
        # Max int – treated as a prime
        self.assertEqual(self.calc.factorize(2147483647), [2147483647])

    def test_invalid_cases(self):
        """Negative inputs should raise an exception."""
        for n in [-1, -10, -2147483648]:
            with self.subTest(n=n):
                with self.assertRaises(ValueError):
                    self.calc.factorize(n)

    def test_singleton(self):
        """Ensure Calculator is a singleton."""
        c1 = Calculator()
        c2 = Calculator()
        self.assertIs(c1, c2)

if __name__ == "__main__":
    unittest.main()
