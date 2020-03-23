import unittest
from src.ch_5_products_and_coproducts import first, second


class TestProductso(unittest.TestCase):

    def test_products(self):
        p = (1, 2)
        self.assertEqual(first(p), 1)
        self.assertEqual(second(p), 2)


if __name__ == '__main__':
    unittest.main()
