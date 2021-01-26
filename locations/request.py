import sqlite3
import json
from models import Location

def get_all_locations():
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # write the SQL QUERY
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM location l
        """)
        # inittialize new empty LIST to hold all the emp DICTs
        locations = []
        # convert rows of data into a PYTHON LIST
        dataset = db_cursor.fetchall()
        # iterate the list
        for row in dataset:
            location = Location(row['id'], row['name'],
                                row['address'])
            locations.append(location.__dict__)
        return json.dumps(locations)


def get_single_location(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM Location l
        WHERE l.id = ?
        """, (id,))
        data = db_cursor.fetchone()
        location = Location(data['id'], data['name'],
                            data['address'])
        return json.dumps(location.__dict__)


def delete_location(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(""" 
        DELETE FROM Location
        WHERE id = ?
        """, (id, ))

def update_location(id, new_location):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(""" 
        UPDATE Location
            Set
                address = ?
        WHERE id = ?
        """, (new_location['address'], id, ))
        # count the rows affected and check if the id provided exists
        rows_affected = db_cursor.rowcount
    if rows_affected == 0:
        # forces 404 response by the main module
        return False
    else:
        # forces 204 response
        return True

def create_location(location):
    # get id value of the LAST LOCATION IN THE LISIIIIIISSSST
    max_id = LOCATIONS[-1]["id"]
    # Add 1 to whatever that number is
    new_id = max_id + 1
    # add an 'id' property to the location DICTIONARY
    location["id"] = new_id
    # add the location dict. to the pre-existing LOCATIONS list
    LOCATIONS.append(location)
    # return the dictionary JUST CREATED, but now with added & appropriate 'id' property
    return location