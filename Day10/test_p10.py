import unittest
from p10 import *

class TestP10(unittest.TestCase):        
    def test_p10_example(self):
        self.assertEqual( p10('example.txt'), 35) 

    def test_p10_example2(self):
        self.assertEqual( p10('example2.txt'), 220) 

    def test_p10_2_example(self):
        self.assertEqual( p10_2('example.txt'), 8) 

    def test_p10_2_example2(self):
        self.assertEqual( p10_2('example2.txt'), 19208)     
     
if __name__ == '__main__':
    unittest.main()
