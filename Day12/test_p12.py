import unittest
from p12 import *

class TestP12(unittest.TestCase):
	def test_changeDirection(self):
		self.assertEqual(changeDirection('E','R',90),'S')
		self.assertEqual(changeDirection('E','R',180),'W')
		self.assertEqual(changeDirection('E','R',270), changeDirection('E','L',90))
		self.assertEqual(changeDirection('N','R',180),'S')
		self.assertEqual(changeDirection('W','L',90),'S')
		self.assertEqual(changeDirection('S','L',270),'W') 
		self.assertEqual(changeDirection('S','L',90),'E')

	def test_p12_example(self):
		self.assertEqual( p12('example.txt'), 25)

	def test_p12_2_example(self):
		self.assertEqual( p12_2('example.txt'), 286)

if __name__ == '__main__':
    unittest.main()
