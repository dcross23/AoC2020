import unittest
from p15 import *

class TestP15(unittest.TestCase):
	def test_p15_example2(self):
		self.assertEqual( p15('examples/example.txt'), 436)
		self.assertEqual( p15('examples/example2.txt'), 1)
		self.assertEqual( p15('examples/example3.txt'), 10)
		self.assertEqual( p15('examples/example4.txt'), 27)
		self.assertEqual( p15('examples/example5.txt'), 78)
		self.assertEqual( p15('examples/example6.txt'), 438)
		self.assertEqual( p15('examples/example7.txt'), 1836)

	def test_p15_2_example2(self):
		self.assertEqual( p15_2('examples/example.txt'), 175594)
		self.assertEqual( p15_2('examples/example2.txt'), 2578)
		self.assertEqual( p15_2('examples/example3.txt'), 3544142)
		self.assertEqual( p15_2('examples/example4.txt'), 261214)
		self.assertEqual( p15_2('examples/example5.txt'), 6895259)
		self.assertEqual( p15_2('examples/example6.txt'), 18)
		self.assertEqual( p15_2('examples/example7.txt'), 362)
        
if __name__ == '__main__':
    unittest.main()
