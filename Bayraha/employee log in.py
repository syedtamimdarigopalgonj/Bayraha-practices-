from datetime import datetime

# import customer_graph

try:
    class employee_info():

        def name_info(self):  # Include 'self' as the first argument in all methods
            first_namme = input('Enter Your First Name: ')
            sur_name = input('Enter the Surname: ')
            name = first_namme + ' ' + sur_name  # Added a space between the names
            name = name.title()

            return name

        def identity_info(self):
            Phone=input('Enter the phone number:')
            Phone=int(Phone)
            email=input('Enter the Email address:')



    # Create an object of the class
    obj = employee_info()

    # Call the methods using the object
    full_name = obj.name_info()  # Call the name_info method
    print("Full Name:", full_name)

    obj.identity_info()  # Call the identity_info method
    # Correct way to get the current time
    current_time = datetime.now()
    print("You have started work at:", current_time.time())
    print( 'Today is',current_time.day)
    print('The date is',current_time.date())
    print('Enjoy the time')
except Exception as e:
    print('You got an error:',e)

