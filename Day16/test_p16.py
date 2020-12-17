import unittest
from p16 import *

class TestP16(unittest.TestCase):
	def test_p16_example(self):
		self.assertEqual( p16('example.txt'), (71,[[7, 3, 47]]))

	def test_p16_2_example2(self):
		#0 because there is no departures so it will return 'result = 1'
		self.assertEqual( p16_2('example2.txt', [[3,9,18],[15,1,5],[5,14,9]]), 1)
			
if __name__ == '__main__':
    unittest.main()
