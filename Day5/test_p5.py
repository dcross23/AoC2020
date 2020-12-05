import unittest
from p5 import *

class TestP5(unittest.TestCase):        
    def test_p5_example(self):
        ids = [357,567,119,820]
        self.assertEqual( p5('example.txt'), (820, ids))  
        
    def test_p5_2_example(self):
        ids = [357,567,119,121,820]
        self.assertEqual( p5_2(ids), 120)      
        
if __name__ == '__main__':
    unittest.main()
