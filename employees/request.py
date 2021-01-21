import sqlite3
import json
from models import Employee


def get_all_employees():
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # write the SQL QUERY
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.location_id,
            e.address
        FROM employee e
        """)
        # inittialize new empty LIST to hold all the emp DICTs
        employees = []
        # convert rows of data into a PYTHON LIST
        dataset = db_cursor.fetchall()
        # iterate the list
        for row in dataset:
            employee = Employee(row['id'], row['name'],
                                row['location_id'],
                                row['address'])
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
            e.address
        FROM Employee e
        WHERE e.id = ?
        """, (id,))
        data = db_cursor.fetchone()
        employee = Employee(data['id'], data['name'], data['location_id'],
                            data['address'])
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
                address = ?
        WHERE id = ?
        """, (new_employee['name'], new_employee['locationId'],
                new_employee['address'], id, ))
        # count the rows affected and check if the id provided exists
        rows_affected = db_cursor.rowcount
    if rows_affected == 0:
        # forces 404 response by the main module
        return False
    else:
        # forces 204 response
        return True

def create_employee(employee):
    # get id value of the LAST EMPLOYEE IN THE LISIIIIIISSSST
    max_id = EMPLOYEES[-1]["id"]
    # Add 1 to whatever that number is
    new_id = max_id + 1
    # add an 'id' property to the employee DICTIONARY
    employee["id"] = new_id
    # add the employee dict. to the pre-existing EMPLOYEES list
    EMPLOYEES.append(employee)
    # return the dictionary JUST CREATED, but now with added & appropriate 'id' property
    return employee