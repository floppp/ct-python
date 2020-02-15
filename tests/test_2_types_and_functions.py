import unittest
from src.ch_2_types_and_functions import factorial, fact


class TestTypesFuncionts(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertNotEqual(factorial(5), 121)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)

    def test_factorial_empty(self):
        self.assertEqual(fact(1), 1)
        self.assertEqual(fact(2), 2)
        self.assertEqual(fact(5), 120)
        self.assertNotEqual(fact(5), 121)


if __name__ == '__main__':
    unittest.main()
