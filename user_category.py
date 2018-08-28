#import the datetime python package to hel us get the current year
import datetime

#get current time
current_time = datetime.datetime.now()

#pick current year
current_year = current_time.year

#prompt user to enter their year of birth
birth_year = int(input("Enter your year of birth (eg 2000):"))

#make sure user enters only int values
def only_int(birth_year):
    try: 
        if type(birth_year) == "int": 
            #current the determinant value
            user_category_value = current_year - birth_year
            return user_category_value
        else: 
           print("Sorry, please enter year in numbers")
           return False
    except ValueError:
        return False

#define function to determine the user category
def user_type(user_category_value):
    if user_category_value < 18:
        print("Your user category is: Minor")
        return

    elif user_category_value <= 36:
        print("Your user category is: Youth")
        return
    
    elif user_category_value <= 0:
        print("Your Entered a negative value")
        return

    elif user_category_value > 36:
        print("Your user category is: Elder")
        return
    else:
        print("Please re-enter your year of birth")
        return False

#display user category
user_type(user_category_value)