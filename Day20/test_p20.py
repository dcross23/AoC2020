import unittest
from p20 import *

class TestP20(unittest.TestCase):
	def test_p20_example(self):
		self.assertEqual( p20('example.txt'), 20899048083289)

	def test_rotate(self):
		self.assertEqual( rotate(['123','456','789']), ['741', '852', '963'])

	def test_flip(self):
		self.assertEqual( flip(['123','456','789']), ['789', '456', '123'])

	def test_getMonsterCoordinates(self):
		monster = ['       # ',
				   '#     #  ',
				   ' #  #  # ']
		coordinates = [(1,-7),(1,-1),(2,-6),(2,-3),(2,0)]
		self.assertEqual( getMonsterCoordinates(monster), coordinates)

	def test_p20_2_example(self):
		self.assertEqual( createTilesImage('example.txt'), 273)

if __name__ == '__main__':
    unittest.main()
