import unittest
from p13 import *

class TestP13(unittest.TestCase):
	def test_p13_example(self):
		self.assertEqual( p13('examples/example.txt'), 295)

	def test_p13_2_examples(self):
		self.assertEqual( p13_2('examples/example.txt'), 1068781)
		self.assertEqual( p13_2('examples/example2.txt'), 3417)
		self.assertEqual( p13_2('examples/example3.txt'), 754018)
		self.assertEqual( p13_2('examples/example4.txt'), 779210)
		self.assertEqual( p13_2('examples/example5.txt'), 1261476)
		self.assertEqual( p13_2('examples/example6.txt'), 1202161486)

if __name__ == '__main__':
    unittest.main()
