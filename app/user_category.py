#import the datetime python package to help us get the current year
import datetime

#get current time
current_time = datetime.datetime.now()
    
#pick current year
current_year = current_time.year

 #find the user category from the user_age values provided      
def user_category(user_value):

    if user_value < 18:
        cat_message = "Your user category is: Minor"
                    
    elif user_value <= 36:
        cat_message = "Your user category is: Youth"
                    
    else:
        cat_message = "Your user category is: Elder"
                
    return cat_message

#make sure only int values are processed
def user_age(birth_year):
        if type(birth_year) != int:
            raise ValueError("Sorry, please enter year in numbers")
           
        if birth_year < 0:
            return "Your Entered a negative value"
            
        elif birth_year > current_year:
            return "You cannot be born in future "
            
        elif birth_year < 1800:
            return "You must be dead by now"
        user_category_value = current_year - birth_year
            
        return user_category(user_category_value)
 

if __name__ == "__main__":
    #prompt user to enter their year of birth
    birth_year = int(input("Enter your year of birth (eg 2000):"))
    print(user_age(birth_year)) 