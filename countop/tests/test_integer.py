from unittest import TestCase
from countop import Integer


class TestInteger(TestCase):
    def test_reset_counts(self):
        Integer.reset_counts()
        for value in Integer.counts.values():
            self.assertTrue(value == 0)

    def test_addition_counts(self):
        x = Integer.additions()
        n = Integer(2)
        n = n + 2
        self.assertTrue(Integer.additions() - x == 1)




