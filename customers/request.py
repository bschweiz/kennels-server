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
        SELECT  
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        FROM Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            customer = Customer(row['id'], row['name'], 
                                row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)

def delete_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(""" 
        DELETE FROM Customer
        WHERE id = ?
        """, (id, ))

def update_customer(id, new_customer):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(""" 
        UPDATE Customer
            Set
                name = ?,
                address = ?,
                email = ?,
                password = ?
        WHERE id = ?
        """, (new_customer['name'], new_customer['address'],
                new_customer['email'], new_customer['password'], id, ))
        # count the rows affected and check if the id provided exists
        rows_affected = db_cursor.rowcount
    if rows_affected == 0:
        # forces 404 response by the main module
        return False
    else:
        # forces 204 response
        return True

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