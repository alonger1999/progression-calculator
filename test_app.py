import unittest

from functions import get_an, get_summa


class ProgressionCalculatorTest(unittest.TestCase):

    def test_get_an(self):

        self.assertEqual(get_an(1, 1, 3), 3)
        self.assertEqual(get_an(2, 0, 5), 2)
        self.assertEqual(get_an(5, 2, 3), 9)
        self.assertEqual(get_an(1, -3, 4), -8)

    def test_get_summa(self):

        self.assertEqual(get_summa(3, 3, 5), 15)
        self.assertEqual(get_summa(0, 0, 1), 0)
        self.assertEqual(get_summa(1, 5, 5), 15)
        self.assertEqual(get_summa(-2, 2, 5), 0)


if __name__ == '__main__':
    unittest.main()
