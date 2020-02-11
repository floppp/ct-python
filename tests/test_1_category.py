import unittest
from typing import TypeVar, Callable, List
from src.category import compose


class TestCategory(unittest.TestCase):

    def setUp(self):
        self.f_impl: Callable[[str], int] = lambda x: int(x)
        self.g_impl: Callable[[int], float] = lambda x: x * 1.0
        self.h_impl: Callable[[float], list] = lambda x: [x]

    def test_f_implementation(self):
        self.assertEqual(2, self.f_impl('2'))

    def test_g_implementation(self):
        self.assertEqual(2.0, self.g_impl(2))

    def test_h_implementation(self):
        self.assertEqual([2.0], self.h_impl(2.0))

    def test_gf_composition(self):
        gf = compose(self.g_impl, self.f_impl)
        self.assertEquals(gf('2'), 2.0)
        self.assertEquals(gf('2'), self.g_impl(self.f_impl('2')))

    def test_h_gf_composition(self):
        gf = compose(self.g_impl, self.f_impl)
        h_fg = compose(self.h_impl, gf)
        self.assertEquals(h_fg('2'), [2.0])
        self.assertEquals(h_fg('2'), self.h_impl(
            self.g_impl(self.f_impl('2'))))

    def test_hg_composition(self):
        hg = compose(self.h_impl, self.g_impl)
        self.assertEquals(hg(2), [2.0])
        self.assertEquals(hg(2), self.h_impl(self.g_impl(2)))

    def test_hg_f_composition(self):
        hg = compose(self.h_impl, self.g_impl)
        hg_f = compose(hg, self.f_impl)
        gf = compose(self.g_impl, self.f_impl)
        h_fg = compose(self.h_impl, gf)
        self.assertEquals(hg_f('2'), [2.0])
        self.assertEquals(hg_f('2'), self.h_impl(
            self.g_impl(self.f_impl('2'))))
        self.assertEquals(hg_f('2'), h_fg('2'))


if __name__ == '__main__':
    unittest.main()
