ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4,
        "status": "Admitted"
    },
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2,
        "status": "Admitted"
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1,
        "status": "Admitted"
    }
]


def get_all_animals():
    return ANIMALS
# Function with a single parameter


def get_single_animal(id):
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal


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
    # initial -1 value for animal index, in case one isn't found
    animal_index = -1
    # iterate the ANIMALS list, but use !!!enumerate()!!! so that
    # you can access the index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. store the current index.
            animal_index = index
    # if the animal was found, use !!!pop(int)!!! to remove it from the list
    if animal_index >= 0:
        ANIMALS.pop(animal_index)

def update_animal(id, new_animal):
    # iterate the ANIMALS list, but use !!!!enumerate() so that
    #you can access the index value of each item.
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # found the proper ANIMAL now update it
            ANIMALS[index] = new_animal
            break