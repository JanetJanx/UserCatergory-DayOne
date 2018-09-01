from user_category import user_type
import unittest

class UserTests(unittest.TestCase):

    def test_usertype(self):
        self.assertEqual(user_type(20), 'Your user category is: Youth')
        self.assertEqual(user_type(54), 'Your user category is: Elder')
        self.assertEqual(user_type(16), 'Your user category is: Minor')

if __name__== '__main__':
    unittest.main()