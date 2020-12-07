import unittest
from p7 import *

class TestP7(unittest.TestCase):        
    def test_p7_example(self):
        self.assertEqual( p7('example.txt'), 4)  

    def test_p7_2_example(self):
        self.assertEqual( p7_2('example.txt'), 32)  
     
    def test_p7_2_example2(self):
        self.assertEqual( p7_2('example2.txt'), 126)  
     

     
if __name__ == '__main__':
    unittest.main()
