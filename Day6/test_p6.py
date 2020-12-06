import unittest
from p6 import *

class TestP6(unittest.TestCase):        
    def test_p6_example(self):
        self.assertEqual( p6('example.txt'), 11)  
        
    def test_p6_2_example(self):
        self.assertEqual( p6_2('example.txt'), 6)      
if __name__ == '__main__':
    unittest.main()
