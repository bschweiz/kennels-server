import sqlite3
import json
from models import Customer

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
        FROM Customer c
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
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.email,
            c.password
        FROM customer c
        WHERE c.id = ?
        """, (id,))
        data = db_cursor.fetchone()
        customer = Customer(data['id'], data['name'],
                            data['email'], data['password'])
        return json.dumps(customer.__dict__)

def get_customers_by_email(email):
    with sqlite3.connect('./kennel.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # Write teh SQL query to get the information you want
        db_cursor.execute("""
        select  
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?

        """, ( email, ))

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
    # you can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. store the current index.
            customer_index = index
    # if the customer was found, use !!!pop(int)!!! to remove it from the list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)


def update_customer(id, new_customer):
    # iterate the CUSTOMERS list, but use !!!!enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # found the proper CUSTOMER now update it
            CUSTOMERS[index] = new_customer
            break
