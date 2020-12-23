import unittest
from p21 import *

class TestP21(unittest.TestCase):
	def test_p21_example(self):
		self.assertEqual( p21('example.txt',1), 5)

	def test_p21_2_example(self):
		self.assertEqual( p21_2('example.txt',2), 'mxmxvkd,sqjhc,fvjkl')

if __name__ == '__main__':
    unittest.main()
