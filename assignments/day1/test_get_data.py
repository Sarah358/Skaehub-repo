import unittest
import get_data
import csv


class TestGetdata(unittest.TestCase):
    def test_data(self):
        info = ''
        result = get_data.main(info)
        self.assertEqual(result,dict(info))


if __name__ == '__main__':
    unittest.main() 


