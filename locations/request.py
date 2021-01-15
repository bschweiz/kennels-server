LOCATIONS = [
    {
      "id": 1,
      "name": "Nashville North",
      "address": "8422 Johnson Pike"
    },
    {
      "id": 2,
      "name": "Nashville South",
      "address": "209 Emory Drive"
    }
  ]

def get_all_locations():
    return LOCATIONS
# Function with a single parameter
def get_single_location(id):
    # Variable to hold the found location, if it exists
    requested_location = None

    # Iterate the LOCATIONS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location

    return requested_location

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
    #you can access the index value of each item
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. store the current index.
            location_index = index
    # if the location was found, use !!!pop(int)!!! to remove it from the list
    if location_index >= 0:
        LOCATIONS.pop(location_index)

def update_location(id, new_location):
    # iterate the LOCAIONS list, but use !!!!enumerate() so that
    #you can access the index value of each item.
    for index, location in enumerate(LOCAIONS):
        if location["id"] == id:
            # found the proper LOCAION now update it
            LOCAIONS[index] = new_location
            break