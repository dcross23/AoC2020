import unittest
from p11 import *

class TestP11(unittest.TestCase):        
    def test_p11_example(self):
        self.assertEqual( p11('example.txt', 1), 37) 
     
    def test_p11_2_example(self):
        self.assertEqual( p11_2('example.txt', 2), 26) 

if __name__ == '__main__':
    unittest.main()
