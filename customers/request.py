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