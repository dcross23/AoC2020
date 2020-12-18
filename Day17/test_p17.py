import unittest
from p17 import *

class TestP17(unittest.TestCase):
	def test_p17_example(self):
		self.assertEqual( p17('example.txt',1), 112)
			
	def test_p17_2_example(self):
		self.assertEqual( p17_2('example.txt',2), 848)

if __name__ == '__main__':
    unittest.main()
