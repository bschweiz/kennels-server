from models import location


class Employee():
    
    def __init__(self, id, name, location_id, animal_id):
        self.id = id
        self.name = name
        self.locationId = location_id
        self.animalId = animal_id