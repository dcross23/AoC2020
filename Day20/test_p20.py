import unittest
from p20 import *

class TestP20(unittest.TestCase):
	def test_p20_example(self):
		self.assertEqual( p20('example.txt'), 20899048083289)

if __name__ == '__main__':
    unittest.main()
