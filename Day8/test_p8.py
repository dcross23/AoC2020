import unittest
from p8 import *

class TestP8(unittest.TestCase):        
    def test_p8_example(self):
        self.assertEqual( p8('example.txt'), 5) 
     
    def test_p8_2_example(self):
        self.assertEqual( p8_2('example.txt'), 8)    
     
if __name__ == '__main__':
    unittest.main()
