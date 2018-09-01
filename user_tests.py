import unittest
from unittest.mock import patch

from user_category import user_category, user_age


class UserTests(unittest.TestCase):

    def test_user_category(self):
        """ Tests whether the user_category returns correct category message
         when for the provided age"""
        self.assertEqual(user_category(15), "Your user category is: Minor")
        self.assertEqual(user_category(25), "Your user category is: Youth")
        self.assertEqual(user_category(45), "Your user category is: Elder")

    @patch("builtins.input", return_value=1500)
    def test_user_age_ancient(self, input):
        """ Tests whether the user_age returns a correct message
         when ancient years are input """
        self.assertEqual(user_age(), "You must be dead by now")

    @patch("builtins.input", return_value=2025)
    def test_user_age_future(self, input):
        """ Tests whether the user_age returns a correct message
         when future years are input """
        self.assertEqual(user_age(), "You cannot be born in future ")
    
    @patch("builtins.input", return_value=-20)
    def test_user_age_negative(self, input):
        """ Tests whether the user_age returns a correct message
         when negative years are input """
        self.assertEqual(user_age(), "Your Entered a negative value")
            

if __name__== '__main__':
    unittest.main()