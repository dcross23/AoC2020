import unittest
from p3 import *

class TestP3(unittest.TestCase):        
    def test_p3_example(self):
        self.assertEqual(p3('example.txt',(1,3)), 7)

    def test_p3_2_example(self):
        slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
        self.assertEqual(p3_2('example.txt', slopes), 336)


if __name__ == '__main__':
    unittest.main()
