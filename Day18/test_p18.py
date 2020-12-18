import unittest
from p18 import *

class TestP18(unittest.TestCase):
	def test_p18_example(self):
		self.assertEqual( p18('example.txt',1), 71+51+26+437+12240+13632)

	def test_p18_2_example(self):
		self.assertEqual( p18_2('example.txt',2), 231+51+46+1445+669060+23340)

if __name__ == '__main__':
    unittest.main()
