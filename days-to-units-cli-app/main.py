calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
        return (f"{num_of_days * calculation_to_units} {name_of_unit} are in {num_of_days} days ")
   
    

def validate_and_execute():
    try:
        number_of_input = int(num_of_element)
        if number_of_input > 0:
            calculated_value = days_to_units(number_of_input) 
            print(calculated_value)
        elif number_of_input == 0:
            print("you enter a 0, please enter a positive  number!")
        else:
            print("you enter a negative value, no conversioin for you!")
    except:
        print("your input is not a valid number,please don't ruin my program!")

user_in_input = ""
while user_in_input != "exit":  
    user_in_input = input("hey user, enter a number of daysas a comma separated list and i will convert it to hours!\n")
    for num_of_element in set(user_in_input.split(",")):
        validate_and_execute()
