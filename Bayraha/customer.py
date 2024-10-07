import json

def customers(**persons):
    return persons

# Initialize an empty list to store customer details
customer_list = []

while True:
    name = input('Enter the name: ')
    address = input('Enter the address: ')
    phone = input('What\'s the phone number: ')

    # Add customer details to the customer_list
    customer_list.append(customers(name=name, address=address, phone=phone))

    # Ask if the user wants to add another customer
    more = input("Do you want to add another customer? (yes/no): ").strip().lower()
    if more != 'yes':
        break

# Save customer_list to a JSON file
with open('customers.json', 'w') as json_file:
    json.dump(customer_list, json_file, indent=4)

print("Customer details saved to customers.json")
