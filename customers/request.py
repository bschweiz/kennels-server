import sqlite3
import json
from models import Customer

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
    with sqlite3.connect("./kennel.db") as conn:
      conn.row_factory = sqlite3.Row
      db_cursor = conn.cursor()
      # write the SQL QUERY
      db_cursor.execute("""
      SELECT
        c.id,
        c.name,
        c.email,
        c.password
      FROM customer c
      """)
      # inittialize new empty LIST to hold all the emp DICTs
      customers = []
      # convert rows of data into a PYTHON LIST
      dataset = db_cursor.fetchall()
      # iterate the list
      for row in dataset:
          customer = Customer(row['id'], row['name'], 
                            row['email'], 
                            row['password'])
          customers.append(customer.__dict__)
    return json.dumps(customers)

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
    
def delete_customer(id):
    # initial -1 value for customer index, in case one isn't found
    customer_index = -1
    # iterate the CUSTOMERS list, but use !!!enumerate()!!! so that
    #you can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. store the current index.
            customer_index = index
    # if the customer was found, use !!!pop(int)!!! to remove it from the list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    # iterate the CUSTOMERS list, but use !!!!enumerate() so that
    #you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # found the proper CUSTOMER now update it
            CUSTOMERS[index] = new_customer
            break
