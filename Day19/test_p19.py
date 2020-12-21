import unittest
from p19 import *

class TestP19(unittest.TestCase):
	def test_p19_examples(self):
		self.assertEqual( p19('examples/example.txt'), 1)
		self.assertEqual( p19('examples/example2.txt'), 2)

	def test_p19_2_examples(self):
		self.assertEqual( p19_2('examples/example3.txt'), 12)	

if __name__ == '__main__':
    unittest.main()
