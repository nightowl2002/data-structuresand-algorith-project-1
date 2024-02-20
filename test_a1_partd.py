#
#   Author: Catherine Leung
#   These are the unit tests for functions and classes of a1_partd
#   To use this, run: python test_a1_partd.py

import unittest
from collections import Counter
from a1_partd import get_overflow_list, overflow
from a1_partc import Queue

class A1DTestCase(unittest.TestCase):
    """These are the test cases for functions and classes of a1_partd"""

    def test_get_overflow_list(self):

        def gen_id(row, col):
            return row * 100 + col

        # Test empty grid
        grid = [[0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]]
        result = get_overflow_list(grid)
        self.assertEqual(result, None)

        # Test grid with no overflow
        grid = [[1, 2, 2, 2, 2, 2, 2],
                [2, 3, 3, 3, 3, 3, 2],
                [2, 3, 3, 3, 3, 3, 2],
                [2, 3, 3, 3, 3, 3, 2],
                [2, 3, 3, 3, 3, 3, 2],
                [2, 3, 3, 3, 3, 3, 2],
                [1, 2, 2, 2, 2, 2, 1]]
        result = get_overflow_list(grid)
        self.assertEqual(result, None)

        # Test grid with overflow
        grid = [[-1, -2, -2, -2, -2, -2, -2],
                [-2, -3, -3, -3, -3, -3, -2],
                [-2, -3, -3, -3, -3, -3, -2],
                [-2, -3, -3, -3, -3, -3, -2],
                [-2, -3, -3, -3, -3, -3, -2],
                [-2, -3, -3, -3, -3, -3, -2],
                [-1, -2, -2, -2, -2, -2, -1]]
        result = get_overflow_list(grid)
        self.assertEqual(result, None)

        # Test grid with overflow
        grid = [[2, 0, 0, 0, 0],
                [0, -3, 0, 0, 0],
                [0, 0, -2, 0, 0],
                [-1, 0, 0, 0, 3]]
        correct = [(0, 0), (3, 4)]
        overflow_hash = Counter()
        for coord in correct:
            overflow_hash[gen_id(coord[0], coord[1])] += 1
        result = get_overflow_list(grid)
        self.assertEqual(len(correct), len(result))
        for coord in result:
            self.assertEqual(overflow_hash[gen_id(coord[0], coord[1])], 1)
            overflow_hash[gen_id(coord[0], coord[1])] += 1

        # Test grid with overflow
        grid = [[-2, 0, 0, 0, 0, 0],
                [0, 3, 0, 0, 0, 0],
                [0, 0, 2, 0, 0, 0],
                [1, 0, 0, 0, -3]]
        correct = [(0, 0), (3, 4)]
        overflow_hash = Counter()
        for coord in correct:
            overflow_hash[gen_id(coord[0], coord[1])] += 1
        result = get_overflow_list(grid)
        self.assertEqual(len(correct), len(result))
        for coord in result:
            self.assertEqual(overflow_hash[gen_id(coord[0], coord[1])], 1)
            overflow_hash[gen_id(coord[0], coord[1])] += 1

        # Test grid with overflow
        grid = [[2, 3, 3, 3, 3, 3, 2],
                [3, 4, 4, 4, 4, 4, 3],
                [3, 4, 4, 4, 4, 3],
                [3, 4, 4, 4, 4, 3],
                [2, 3, 3, 3, 3, 2]]
        correct = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
                   (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
                   (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
                   (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
                   (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5)]

