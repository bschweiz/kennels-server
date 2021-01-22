import sqlite3
import json
from sqlite3.dbapi2 import Cursor

from models import Animal
from models.location import Location
from models.customer import Customer


def get_all_animals():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:
        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id,
            l.name location_name,
            l.address location_address,
            c.name cust_name,
            c.address cust_address,
            c.email cust_email
        FROM Animal a
        JOIN Location l
            ON l.id = a.location_id
        JOIN Customer c
            ON c.id = a.customer_id
        """)
        # Initialize an empty list to hold all animal representations
        animals = []
        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()
        # Iterate list of data returned from database
        for row in dataset:
            # Create an animal instance from the current row.
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'], row['customer_id'])
            # Create a location instance for the current row
            location = Location(row['location_id'],row['location_name'], row['location_address'])
            # Create a customer instance for the current row
            customer = Customer(row['customer_id'], row['cust_name'], row['cust_address'], row['cust_email'])
            # Add the dictionary representations of the location and customer to the animal
            animal.location = location.__dict__
            animal.customer = customer.__dict__
            animals.append(animal.__dict__)
    # Use `json` package to properly serialize list as JSON
    return json.dumps(animals)


def get_single_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM Animal a
        WHERE a.id = ?
        """, (id, ))
        # Load the single result into memory
        data = db_cursor.fetchone()
        # Create an animal instance from the current row
        animal = Animal(data['id'], data['name'], data['breed'],
                        data['status'], data['location_id'],
                        data['customer_id'])
        return json.dumps(animal.__dict__)


def get_animals_by_location(location_id):
    with sqlite3.connect('./kennel.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # write the SQL query with the location_id is inserted into the WHERE clause
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM Animal a
        WHERE a.location_id = ? 
        """, (location_id, ))
# "?" references second argument of the .execute method, in this instance
# location_id
        animals = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            animal = Animal(row['id'], row['name'],
                            row['breed'], row['status'], row['location_id'],
                            row['customer_id'])
            animals.append(animal.__dict__)
    return json.dumps(animals)


def get_animals_by_status(status):
    with sqlite3.connect('./kennel.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # write the SQL query with the status is inserted into the WHERE clause
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM Animal a
        WHERE a.status = ? 
        """, (status, ))
# "?" references second argument of the .execute method, in this instance
# status
        animals = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            animal = Animal(row['id'], row['name'],
                            row['breed'], row['status'], row['location_id'],
                            row['customer_id'])
            animals.append(animal.__dict__)
    return json.dumps(animals)


def delete_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(""" 
        DELETE FROM Animal
        WHERE id = ?
        """, (id, ))


def update_animal(id, new_animal):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(""" 
        UPDATE Animal
            Set
                name = ?,
                breed = ?,
                status = ?,
                location_id = ?,
                customer_id = ?
        WHERE id = ?
        """, (new_animal['name'], new_animal['breed'],
              new_animal['status'], new_animal['locationId'],
              new_animal['customerId'], id, ))
        # count the rows affected and check if the id provided exists
        rows_affected = db_cursor.rowcount
    if rows_affected == 0:
        # forces 404 response by the main module
        return False
    else:
        # forces 204 response
        return True


def create_animal(animal):
    # get id value of the LAST ANIMAL IN THE LISIIIIIISSSST
    max_id = ANIMALS[-1]["id"]
    # Add 1 to whatever that number is
    new_id = max_id + 1
    # add an 'id' property to the animal DICTIONARY
    animal["id"] = new_id
    # add the animal dict. to the pre-existing ANIMALS list
    ANIMALS.append(animal)
    # return the dictionary JUST CREATED, but now with added & appropriate 'id' property
    return animal
