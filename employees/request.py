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
    return EMPLOYEES
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
    