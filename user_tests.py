import user_category
import unittest

class UserTests(unittest.TestCase):
    
    def test_number(self):
        result = user_category.number()
        self.assertEqual(result, 2000)
    
    def test_usertype(self):
        res = user_category.user_type(2000)
        self.assertEqual(res, "Your user category is: Elder")

if __name__== '__main__':
    unittest.main()