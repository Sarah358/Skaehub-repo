import unittest
from unittest import result
import length

class TestLength(unittest.TestCase):
    # test function
    def test_len_last_word(self):
        a = 'Hello world' 
        result = length.len_last_word(a)
        self.assertEqual(result,5)

    # if size== 1 return length of that word
    def test_is_one_word(self):
        b = 'Hey'
        result = length.len_last_word(b)
        self.assertEqual(result,3)
    

if __name__ == '__main__':
    unittest.main()


