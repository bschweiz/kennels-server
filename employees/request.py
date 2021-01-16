import sqlite3
import json
from models import Employee

EMPLOYEES = [
    {
      "name": "Ashton",
      "locationId": 1,
      "animalId": 3,
      "id": 1
    },
    {
      "name": "Hickley",
      "locationId": 2,
      "animalId": 3,
      "id": 2
    },
    {
      "name": "Michael",
      "locationId": 1,
      "animalId": 2,
      "id": 3
    }
]

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

# Function with a single parameter
def get_single_employee(id):
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the EMPLOYEES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

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
  
def delete_employee(id):
  # initial -1 value for employee index, in case one isn't found
  employee_index = -1
  # iterate the EMPLOYEES list, but use !!!enumerate()!!! so that
  #you can access the index value of each item
  for index, employee in enumerate(EMPLOYEES):
      if employee["id"] == id:
          # Found the employee. store the current index.
          employee_index = index
  # if the employee was found, use !!!pop(int)!!! to remove it from the list
  if employee_index >= 0:
      EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
  # iterate the EMPLOYEES list, but use !!!!enumerate() so that
  #you can access the index value of each item.
  for index, employee in enumerate(EMPLOYEES):
      if employee["id"] == id:
          # found the proper CUSTOMER now update it
          EMPLOYEES[index] = new_employee
          break