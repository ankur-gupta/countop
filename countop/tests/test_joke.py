from unittest import TestCase
import countop as co


class TestJoke(TestCase):
    def test_is_string(self):
        s = co.joke()
        self.assertTrue(isinstance(s, str))

