import unittest
from p25 import *

class TestP25(unittest.TestCase):
	def test_p25_example(self):
		self.assertEqual( p25('example.txt'), 14897079)

if __name__ == '__main__':
    unittest.main()
