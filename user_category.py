#import the datetime python package to help us get the current year
import datetime

#get current time
current_time = datetime.datetime.now()
    
#pick current year
current_year = current_time.year

#make sure only int values are processed
def user_age():
        try:
            #prompt user to enter their year of birth
            birth_year = int(input("Enter your year of birth (eg 2000):"))
            user_category_value = current_year - birth_year

        except ValueError:
            return "Sorry, please enter year in numbers"
           
        if birth_year < 0:
            return "Your Entered a negative value"
            
        elif birth_year > current_year:
            return "You cannot be born in future "
            
        elif birth_year < 1800:
            return "You must be dead by now"
            
        return user_category(user_category_value)

 #find the user category from the user_age values provided      
def user_category(user_value):

    if user_value < 18:
        cat_message = "Your user category is: Minor"
                    
    elif user_value <= 36:
        cat_message = "Your user category is: Youth"
                    
    else:
        cat_message = "Your user category is: Elder"
                
    return cat_message

#display user category
print(user_age())   