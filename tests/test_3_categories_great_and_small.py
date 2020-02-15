import unittest
from src.ch_3_categories_great_and_small import String, sd_combine, sd_empty


class TestCaegoriesGreatAndSmall(unittest.TestCase):

    def test_string_monoid(self):
        s = String()
        self.assertEqual(s.empty(), '')
        self.assertEqual(s.combine('a', 'b'), 'ab')
        self.assertEqual(sd_empty('a'), '')
        self.assertEqual(sd_combine('a', 'b'), 'ab')
        self.assertNotEqual(sd_combine('a', 'b'), 'abc')


if __name__ == '__main__':
    pass
