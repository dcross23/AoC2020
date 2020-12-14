import unittest
from p14 import *

class TestP14(unittest.TestCase):
	def test_p14_example(self):
		self.assertEqual( p14('example.txt',1), 165)

	def test_p14_2_example(self):
		self.assertEqual( p14_2('example2.txt',2), 208)

if __name__ == '__main__':
    unittest.main()
