import unittest

from app.user_category import user_category, user_age


class TestUser(unittest.TestCase):

    def test_user_category_minor(self):
        """ Tests whether the user_category returns correct category message for minor"""
        self.assertEqual(user_category(15), "Your user category is: Minor")

    def test_user_category_youth(self):
        """ Tests whether the user_category returns correct category message for youth"""
        self.assertEqual(user_category(25), "Your user category is: Youth")

    def test_user_category_elder(self):
        """ Tests whether the user_category returns correct category message for elder"""
        self.assertEqual(user_category(45), "Your user category is: Elder")

    def test_user_age_ancient(self):
        """ Tests whether the user_age returns a correct message
         when ancient years are input """
        self.assertEqual(user_age(1500), "You must be dead by now")

    def test_user_age_future(self):
        """ Tests whether the user_age returns a correct message
         when future years are input """
        self.assertEqual(user_age(2025), "You cannot be born in future ")
    
    def test_user_age_negative(self):
        """ Tests whether the user_age returns a correct message
         when negative years are input """
        self.assertEqual(user_age(-20), "Your Entered a negative value")
    
    def test_user_age_non_interger(self):
        with self.assertRaises(ValueError):
            user_age('wer')
            

if __name__== '__main__':
    unittest.main()