#
#   Author: Catherine Leung
#   These are the unit tests for functions and classes of assignment 1 part C
#   To use this, run: python test\_a1\_partc.py

import unittest
from a1\_partc import Stack, Queue, Deque

class A1CTestCase(unittest.TestCase):
    """
    These are the test cases for functions and classes of assignment 1 part C
    """

    def test_stack_init(self):
        """
        Testing the initialization of the Stack class
        """
        the_stack = Stack()
        self.assertEqual(len(the_stack), 0)
        self.assertEqual(the_stack.is_empty(), True)
        self.assertEqual(the_stack.get_top(), None)
        self.assertEqual(the_stack.capacity(), 10)

        second_stack = Stack(17)
        self.assertEqual(len(second_stack), 0)
        self.assertEqual(second_stack.is_empty(), True)
        self.assertEqual(second_stack.get_top(), None)
        self.assertEqual(second_stack.capacity(), 17)

    def test_stack_push(self):
        """
        Testing the push method of the Stack class
        """
        the_stack = Stack(5)
        the_stack.push(1)
        self.assertEqual(the_stack.is_empty(), False)
        self.assertEqual(len(the_stack), 1)
        self.assertEqual(the_stack.get_top(), 1)
        self.assertEqual(the_stack.capacity(), 5)

        the_stack.push(5)
        self.assertEqual(the_stack.is_empty(), False)
        self.assertEqual(len(the_stack), 2)
        self.assertEqual(the_stack.get_top(), 5)
        self.assertEqual(the_stack.capacity(), 5)

        the_stack.push(10)
        self.assertEqual(the_stack.is_empty(), False)
        self.assertEqual(len(the_stack), 3)
        self.assertEqual(the_stack.get_top(), 10)

        the_stack.push(8)
        self.assertEqual(the_stack.is_empty(), False)
        self.assertEqual(len(the_stack), 4)
        self.assertEqual(the_stack.get_top(), 8)
        self.assertEqual(the_stack.capacity(), 5)

        for i in range(1000):
            the_stack.push(i)
            self.assertEqual(the_stack.is_empty(), False)
        self.assertEqual(len(the_stack), 1004)
        self.assertEqual(the_stack.get_top(), 999)
        self.assertEqual(the_stack.is_empty(), False)
        self.assertEqual(the_stack.capacity(), 1280)

    def test_stack_pop(self):
        """
        Testing the pop method of the Stack class
        """
        the_stack = Stack(5)
        the_stack.push(1)
        the_stack.push(5)
        the_stack.push(10)
        the_stack.push(8)

        rc = the_stack.pop()
        self.assertEqual(the_stack.is_empty(), False)
        self.assertEqual(len(the_stack), 3)
        self.assertEqual(the_stack.get_top(), 10)
        self.assertEqual(rc, 8)
        self.assertEqual(the_stack.capacity(), 5)

        rc = the_stack.pop()
        self.assertEqual(the_stack.is_empty(), False)
        self.assertEqual(len(the_stack), 2)
        self.assertEqual(the_stack.get_top(), 5)
        self.assertEqual(rc, 10)
        self.assertEqual(the_stack.capacity(), 5)

        rc = the_stack.pop()
        self.assertEqual(the_stack.is_empty(), False)
        self.assertEqual(len(the_stack), 1)
        self.assertEqual(the_stack.get_top(), 1)
        self.assertEqual(rc, 5)
        self.assertEqual(the_stack.capacity(), 5)

        rc = the_stack.pop()
        self.assertEqual(the_stack.is_empty(), True)
        self.assertEqual(len(the_stack), 0)
        self.assertEqual(the_stack.get_top(), None)
        self.assertEqual(rc, 1)
        self.assertEqual(the_stack.capacity(), 5)

        with self.assertRaises(IndexError):
            rc = the_stack.pop()

    def test_queue_init(self):
        """
        Testing the initialization of the Queue class
        """
        the_queue = Queue()
        self.assertEqual(len(the_queue), 0)
        self.assertEqual(the_queue.is_empty(), True)
        self.assertEqual(the_queue.get_front(), None)
        self.assertEqual(the_queue.capacity(), 10)

        second_queue = Queue(8)
        self.assertEqual(len(second_queue), 0)
        self.assertEqual(second_queue.is_empty(), True)
        self.assertEqual(second_queue.get_front(), None)
        self.assertEqual(second_queue.capacity(), 8)

    def test_queue_enqueue(self):
        """
        Testing the enqueue method of the Queue class
        """
        the_queue = Queue(5)
        self.assertEqual(the_queue.capacity(), 5)
        the_queue.enqueue(1)
        self.assertEqual(the_queue.is_empty(), False)
        self.assertEqual(len(the_queue), 1)
        self.assertEqual(the_queue.get_front(), 1)

        the_queue.enqueue(5)
        self.assertEqual(the_queue.capacity(), 5)
        self.assertEqual(the_queue.is_empty(), False
