import unittest

from list_f import flat_function


class FlatListTestCase(unittest.TestCase):

    def setUp(self):
        self.test_data = flat_function([[1, 2, 3], [4, 5], [1]])

    def test_isinstance(self):
        self.assertIsInstance(
            self.test_data, list)

    def test_elements_isint(self):
        for element in self.test_data:
            self.assertIsInstance(element, int)

    def test_equal_list(self):
        self.assertEqual(
            self.test_data, [1, 2, 3, 4, 5, 1])


if __name__ == '__main__':
    unittest.main()
