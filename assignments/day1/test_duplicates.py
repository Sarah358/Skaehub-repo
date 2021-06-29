import unittest
import duplicates

class TestDuplicates(unittest.TestCase):
    def test_rm_duplicate(self):
        fruits = ['oranges','kiwi','apple','kiwi']
        result = duplicates.rm_duplicate(fruits)
        self.assertEqual(result,['oranges','kiwi','apple'])


if __name__ == '__main__':
    unittest.main() 


