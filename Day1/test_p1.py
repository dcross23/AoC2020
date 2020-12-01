import unittest
import itertools
from p1 import *

class TestP1(unittest.TestCase):        
    def test_p1_example(self):
        self.assertEqual(p1('example.txt'), 514579)

    def test_p2_example(self):
        self.assertEqual(p1_2('example.txt'), 241861950)


if __name__ == '__main__':
    unittest.main()
