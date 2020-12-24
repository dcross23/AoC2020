import unittest
from p24 import *

class TestP24(unittest.TestCase):
	def test_p24_example(self):
		self.assertEqual( len(p24('example.txt')), 10)

	def test_p24_2_example(self):
		flippedTiles = [(-3, 1, 2), (-3, 0, 3), (-2, 2, 0), (0, 1, -1), (-2, 1, 1), (3, 0, -3), (0, -2, 2), (0, 0, 0), (2, -2, 0), (-1, 2, -1)]
		self.assertEqual( p24_2(flippedTiles), 2208)

if __name__ == '__main__':
    unittest.main()
