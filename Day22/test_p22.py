import unittest
from p22 import *

class TestP22(unittest.TestCase):
	def test_p22_example(self):
		self.assertEqual( p22('example.txt'), 306)

	def test_p22_2_example(self):
		self.assertEqual( p22_2('example.txt'), 291)	

if __name__ == '__main__':
    unittest.main()
