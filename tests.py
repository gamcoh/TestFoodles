import unittest
from main import sort_by_count_and_alphabetical

class TestSort(unittest.TestCase):
	def test_output(self):
		_input = "baz bar foo foo zblah zblah zblah baz toto bar", 3
		_output = sort_by_count_and_alphabetical(*_input)
		self.assertEqual(_output, [("zblah", 3), ("bar", 2), ("baz", 2)])

if __name__ == "__main__":
	unittest.main()