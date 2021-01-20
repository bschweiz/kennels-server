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
            l.address
        FROM location l
        """)
        # inittialize new empty LIST to hold all the emp DICTs
        locations = []
        # convert rows of data into a PYTHON LIST
        dataset = db_cursor.fetchall()
        # iterate the list
        for row in dataset:
            location = Location(row['id'],
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
            l.address
        FROM location l
        WHERE l.id = ?
        """, (id,))
        data = db_cursor.fetchone()
        location = Location(data['id'],
                            data['address'])
        return json.dumps(location.__dict__)


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


def delete_location(id):
    # initial -1 value for location index, in case one isn't found
    location_index = -1
    # iterate the LOCATIONS list, but use !!!enumerate()!!! so that
    # you can access the index value of each item
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. store the current index.
            location_index = index
    # if the location was found, use !!!pop(int)!!! to remove it from the list
    if location_index >= 0:
        LOCATIONS.pop(location_index)


def update_location(id, new_location):
    # iterate the LOCAIONS list, but use !!!!enumerate() so that
    # you can access the index value of each item.
    for index, location in enumerate(LOCAIONS):
        if location["id"] == id:
            # found the proper LOCAION now update it
            LOCAIONS[index] = new_location
            break
