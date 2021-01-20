import sqlite3
import json
from sqlite3.dbapi2 import Cursor
from models import Animal


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
            a.customer_id
        FROM animal a
        """)
        # Initialize an empty list to hold all animal representations
        animals = []
        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()
        # Iterate list of data returned from database
        for row in dataset:
            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])
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


def delete_animal(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(""" 
        DELETE FROM Animal
        WHERE id = ?
        """, (id, ))


def update_animal(id, new_animal):
    # iterate the ANIMALS list, but use !!!!enumerate() so that
    # you can access the index value of each item.
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # found the proper ANIMAL now update it
            ANIMALS[index] = new_animal
            break
