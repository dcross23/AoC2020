import unittest
from p9 import *

class TestP9(unittest.TestCase):        
    def test_p9_example(self):
        self.assertEqual( p9('example.txt',5), 127) 
     
    def test_p9_example(self):
        self.assertEqual( p9_2('example.txt',127), 62)  

if __name__ == '__main__':
    unittest.main()
