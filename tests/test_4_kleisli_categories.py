import unittest
from src.ch_4_kleisli_categories import Option, optional_composition
from src.ch_4_kleisli_categories import safe_reciprocal
from src.ch_4_kleisli_categories import safe_root
from src.ch_4_kleisli_categories import safe_root_reciprocal


class TestKleislis(unittest.TestCase):

    def test_composition(self):
        def fa(x): return Option(x)
        def fb(x): return Option(2 * x)
        g = optional_composition(fa, fb)

        self.assertEqual(g(4).v, 8)
        self.assertNotEqual(g(4).v, 6)

        def fa(x): return Option(None)
        g = optional_composition(fa, fb)
        self.assertIs(g(4).v, None)
        self.assertNotEqual(g(4).v, 8)

    def test_safe_root_reciprocal(self):
        self.assertEqual(safe_reciprocal(2).v, 0.5)
        self.assertEqual(safe_root_reciprocal(4).v, 0.5)
        self.assertNotEqual(safe_root_reciprocal(-4).v, 0.5)
        self.assertIs(safe_root_reciprocal(-4).v, None)
        self.assertIs(safe_root_reciprocal(0).v, None)


if __name__ == '__main__':
    unittest.main()
