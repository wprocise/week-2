import unittest

from gradescope_utils.autograder_utils.decorators import weight, number

from apputil import *


class TestFunction(unittest.TestCase):
    @weight(1)
    @number("1.1")
    def test_ways_basic(self):
        """
        Evaluate a few typical cases:
            12 --> 3
            20 --> 5
            3  --> 1
        """
        self.assertEqual(ways(12), 3, "ways(12) --> 3")
        self.assertEqual(ways(20), 5, "ways(20) --> 5")
        self.assertEqual(ways(3), 1, "ways(3) --> 1")

    @weight(1)
    @number("2.1")
    def test_ways_edge(self):
        """
        Evaluate an edge case:
            0 --> 1
        """
        self.assertEqual(ways(0), 1, "ways(0) --> 1")

    # @weight(2)
    # @number("3.1")
    # def test_exception(self):
    #     """Evaluating 2 ** 8 should raise an exception"""
    #     with self.assertRaises(ValueError):
    #         func("2 ** 8")

    