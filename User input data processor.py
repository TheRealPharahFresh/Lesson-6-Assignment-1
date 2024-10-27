# Task 1: Input Length Validator 
# Write a script that asks for and checks the length of the user's first name and last name.
#  Both should be at least 2 characters long. If not, print an error message.



def input_length_validator():
    print('Hey what is your first name?')
    first_name = input("Enter your first name: ")
    print('Thank you... Now What is your last name?')
    last_name = input("Enter your last name :")

    first_name_length = len(first_name)
    last_name_length = len(last_name)
    return first_name_length, last_name_length


first_length, last_length = input_length_validator()
print(f'The length of your first name is: {first_length}')
print(f'The length of your last name is: {last_length}')
   








