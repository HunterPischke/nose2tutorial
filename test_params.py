import unittest

from nose2.tools import params

@params(1, 2, 3)
def test_even(num):
	assert (num % 2) == 0

class Test(unittest.TestCase):

    @params((1, 2), (2, 3), (4, 5))
    def test_less_than(self, a, b):
        assert a < b
