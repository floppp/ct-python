import unittest
from typing import TypeVar, Callable, List
from src.category import compose
from src.category import f_impl, g_impl, h_impl


class TestCategory(unittest.TestCase):

    # def setUp(self):
    # self.f_impl: Callable[[str], int] = lambda x: int(x)
    # self.g_impl: Callable[[int], float] = lambda x: x * 1.0
    # self.h_impl: Callable[[float], list] = lambda x: [x]

    def test_f_implementation(self):
        self.assertEqual(2, f_impl('2'))

    def test_g_implementation(self):
        self.assertEqual(2.0, g_impl(2))

    def test_h_implementation(self):
        self.assertEqual([2.0], h_impl(2.0))

    def test_gf_composition(self):
        gf = compose(g_impl, f_impl)
        self.assertEquals(gf('2'), 2.0)
        self.assertEquals(gf('2'), g_impl(f_impl('2')))

    def test_h_gf_composition(self):
        gf = compose(g_impl, f_impl)
        h_fg = compose(h_impl, gf)
        self.assertEquals(h_fg('2'), [2.0])
        self.assertEquals(h_fg('2'), h_impl(
            g_impl(f_impl('2'))))

    def test_hg_composition(self):
        hg = compose(h_impl, g_impl)
        self.assertEquals(hg(2), [2.0])
        self.assertEquals(hg(2), h_impl(g_impl(2)))

    def test_hg_f_composition(self):
        hg = compose(h_impl, g_impl)
        hg_f = compose(hg, f_impl)
        gf = compose(g_impl, f_impl)
        h_fg = compose(h_impl, gf)
        self.assertEquals(hg_f('2'), [2.0])
        self.assertEquals(hg_f('2'), h_impl(g_impl(f_impl('2'))))
        self.assertEquals(hg_f('2'), h_fg('2'))


if __name__ == '__main__':
    unittest.main()
