CUSTOMERS = [
    {
      "email": "bob@email.com",
      "password": "blabla",
      "name": "Bob Genius",
      "id": 1
    },
    {
      "email": "sally@email.com",
      "password": "blabla",
      "name": "Sally Genius",
      "id": 2
    },
    {
      "email": "jim@email.com",
      "password": "blabla",
      "name": "Jim Genius",
      "id": 3
    }
]

def get_all_customers():
    return CUSTOMERS
# Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the CUSTOMERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    # get id value of the LAST CUSTOMER IN THE LISIIIIIISSSST
    max_id = CUSTOMERS[-1]["id"]
    # Add 1 to whatever that number is
    new_id = max_id + 1
    # add an 'id' property to the customer DICTIONARY
    customer["id"] = new_id
    # add the customer dict. to the pre-existing CUSTOMERS list
    CUSTOMERS.append(customer)
    # return the dictionary JUST CREATED, but now with added & appropriate 'id' property 
    return customer
    