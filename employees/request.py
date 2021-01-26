import sqlite3
import json
from models import Employee
from models import Location


def get_all_employees():
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # write the SQL QUERY
        db_cursor.execute("""
        SELECT
            e.id emp_id,
            e.name emp_name,
            e.location_id emp_loc,
            e.animal_id,
            l.id loc_id,
            l.name loc_name,
            l.address loc_address
        FROM Employee e
        JOIN Location l
            ON loc_id = emp_loc
        """)
        # inittialize new empty LIST to hold all the emp DICTs
        employees = []
        # convert rows of data into a PYTHON LIST
        dataset = db_cursor.fetchall()
        # iterate the list
        for row in dataset:
            employee = Employee(row['emp_id'], row['emp_name'], row['emp_loc'], row['animal_id'])
            location = Location(row['loc_id'], row['loc_name'], row['loc_address'])
            employee.location = location.__dict__
            employees.append(employee.__dict__)
    return json.dumps(employees)

def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.location_id,
            e.animal_id
        FROM Employee e
        WHERE e.id = ?
        """, (id,))
        data = db_cursor.fetchone()
        employee = Employee(data['id'], data['name'], data['location_id'],
                            data['animal_id'])
        return json.dumps(employee.__dict__)

def get_employees_by_location(location_id):
    with sqlite3.connect('./kennel.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # write the SQL query with the location_id is inserted into the WHERE clause
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.location_id,
            e.address
        FROM Employee e
        WHERE e.location_id = ? 
        """, (location_id, ))
# "?" references second argument of the .execute method, in this instance
# location_id
        employees = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            employee = Employee(row['id'], row['name'], 
                            row['location_id'], row['address'])
            employees.append(employee.__dict__)
    return json.dumps(employees)

def delete_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(""" 
        DELETE FROM Employee
        WHERE id = ?
        """, (id, ))

def update_employee(id, new_employee):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(""" 
        UPDATE Employee
            Set
                name = ?,
                location_id = ?,
                animal_id = ?
        WHERE id = ?
        """, (new_employee['name'], new_employee['locationId'],
                new_employee['animalId'], id, ))
        # count the rows affected and check if the id provided exists
        rows_affected = db_cursor.rowcount
    if rows_affected == 0:
        # forces 404 response by the main module
        return False
    else:
        # forces 204 response
        return True

def create_employee(new_employee):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Employee
            ( name, location_id, animal_id )
        VALUES
            ( ?, ?, ? );
        """, (
                new_employee['name'], 
                new_employee['locationId'], 
                new_employee['animalId'], )
        )
# The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid
        # Add the 'id' property to the employee dict that
        # waws sent by client so client can see the primary key in the repsonse.
        new_employee['id'] = id
    return json.dumps(new_employee)