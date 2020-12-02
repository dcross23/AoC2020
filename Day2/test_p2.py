import unittest
from p2 import *

class TestP2(unittest.TestCase):        
    def test_p2_example(self):
        self.assertEqual(p2('example.txt'), 2)

    def test_p2_2_example(self):
        self.assertEqual(p2_2('example.txt'), 1)


if __name__ == '__main__':
    unittest.main()
