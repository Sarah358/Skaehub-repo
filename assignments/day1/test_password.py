import unittest
import password as test_3

# Test  password length

class TestPassword(unittest.TestCase):
# test for low password
    def test_low_password_length(self):
        password = test_3.password_output(1)
        self.assertEqual(len(password),6)
        # test for medium password
    def test_medium_password_length(self):
        password = test_3.password_output(2)
        self.assertEqual(len(password),8)
        # test for strong password
    def test_strong_password_length(self):
        password = test_3.password_output(3)
        self.assertEqual(len(password),12)
   
if __name__ == '__main__':
    unittest.main()