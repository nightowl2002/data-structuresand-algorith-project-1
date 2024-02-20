#
#   Author: Catherine Leung
#   These are the unit tests for functions and classes of assignment 1 Part B
#   To use this, run: python test_a1_partb.py

import unittest
from a1_partb import SortedList

class A1BTestCase(unittest.TestCase):
    """These are the test cases for functions and classes of a1"""

    def test_init_get_len_empty(self):
        """Test initialization, getting length, and checking if empty for an empty SortedList"""
        my_list = SortedList()
        self.assertEqual(len(my_list), 0)
        self.assertEqual(my_list.is_empty(), True)
        self.assertEqual(my_list.get_front(), None)
        self.assertEqual(my_list.get_back(), None)

    def test_insert(self):
        """Test inserting elements into the SortedList"""
        my_list = SortedList()
        nn = my_list.insert(10)
        self.assertEqual(my_list.is_empty(), False)
        self.assertEqual(len(my_list), 1)
        self.assertNotEqual(my_list.get_front(), None)
        self.assertNotEqual(my_list.get_back(), None)
        self.assertEqual(my_list.get_front().get_data(), 10)
        self.assertEqual(my_list.get_back().get_data(), 10)
        self.assertEqual(nn.get_data(), 10)

        nn = my_list.insert(5)
        self.assertEqual(nn.get_data(), 5)
        self.assertEqual(nn.get_next().get_data(), 10)
        self.assertEqual(nn.get_next().get_previous(), nn)
        self.assertEqual(len(my_list), 2)
        self.assertEqual(my_list.get_front().get_data(), 5)
        self.assertEqual(my_list.get_back().get_data(), 10)
        self.assertEqual(nn.get_next().get_data(), 10)
        self.assertEqual(my_list.get_back().get_previous(), nn)

        nn = my_list.insert(15)
        self.assertEqual(len(my_list), 3)
        self.assertEqual(nn.get_data(), 15)
        self.assertEqual(nn.get_previous().get_data(), 10)
        self.assertEqual(nn.get_previous().get_next(), nn)
        self.assertEqual(my_list.get_front().get_data(), 5)
        self.assertEqual(my_list.get_front().get_next().get_data(), 10)
        self.assertEqual(my_list.get_front().get_next().get_next().get_data(), 15)
        self.assertEqual(my_list.get_back().get_data(), 15)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 10)
        self.assertEqual(my_list.get_back().get_previous().get_previous().get_data(), 5)

        nn = my_list.insert(12)
        self.assertEqual(len(my_list), 4)
        self.assertEqual(nn.get_data(), 12)
        self.assertEqual(nn.get_previous().get_data(), 10)
        self.assertEqual(nn.get_previous().get_next(), nn)
        self.assertEqual(nn.get_next().get_data(), 15)
        self.assertEqual(nn.get_next().get_previous(), nn)
        self.assertEqual(my_list.get_front().get_data(), 5)
        self.assertEqual(my_list.get_front().get_next().get_data(), 7)
        self.assertEqual(my_list.get_front().get_next().get_next().get_data(), 10)
        self.assertEqual(my_list.get_front().get_next().get_next().get_next().get_data(), 12)
        self.assertEqual(my_list.get_front().get_next().get_next().get_next().get_next().get_data(), 15)
        self.assertEqual(my_list.get_back().get_data(), 15)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 12)
        self.assertEqual(my_list.get_back().get_previous().get_previous().get_data(), 10)
        self.assertEqual(my_list.get_back().get_previous().get_previous().get_previous().get_data(), 5)

        nn = my_list.insert(7)
        self.assertEqual(len(my_list), 5)
        self.assertEqual(nn.get_data(), 7)
        self.assertEqual(nn.get_previous().get_data(), 5)
        self.assertEqual(nn.get_previous().get_next(), nn)
        self.assertEqual(nn.get_next().get_data(), 10)
        self.assertEqual(nn.get_next().get_previous(), nn)
        self.assertEqual(my_list.get_front().get_data(), 5)
        self.assertEqual(my_list.get_front().get_next().get_data(), 7)
        self.assertEqual(my_list.get_front().get_next().get_next().get_data(), 10)
        self.assertEqual(my_list.get_back().get_data(), 15)
        self.assertEqual(my_list.get_back().get_previous().get_data(), 12)
        self.assertEqual(my_list.get_back().get_previous().get_previous().get_data(), 10)
        self.assertEqual(my_list.get_back().get_previous().get_previous().get_previous().get_data(), 5)

        my_data = [4,8,6,7,1, 3,5,10,
