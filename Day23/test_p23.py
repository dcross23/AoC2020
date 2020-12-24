import unittest
from p23 import *

class TestP23(unittest.TestCase):
	def test_p23_example(self):
		self.assertEqual( p23('example.txt',10), '92658374')
		self.assertEqual( p23('example.txt',100), '67384529')

if __name__ == '__main__':
    unittest.main()
