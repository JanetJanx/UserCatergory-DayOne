#import the datetime python package to help us get the current year
import datetime

#get current time
current_time = datetime.datetime.now()

#pick current year
current_year = current_time.year

#make sure user enters only int values
def number():
    while True:
        try:
            #prompt user to enter their year of birth
            birth_year = int(input("Enter your year of birth (eg 2000):"))
        except ValueError:
            print("Sorry, please enter year in numbers")
            continue
        if birth_year < 0:
            print("Your Entered a negative value")
            continue
        elif birth_year > current_year:
            print("You cannot be born in future ")
            continue
        elif birth_year < 1800:
            print("You must be dead by now")
            continue
        else:
            return birth_year
            break

#the determinant value
user_category_value = current_year - number()

#define function to determine the user category
def user_type(user_category_value):
    if user_category_value < 18:
        print("Your user category is: Minor")
        return

    elif user_category_value <= 36:
        print("Your user category is: Youth")
        return

    elif user_category_value > 36:
        print("Your user category is: Elder")
        return
    else:
        print("Sorry, please re-enter year in numbers")
        return False

#display user category
user_type(user_category_value)