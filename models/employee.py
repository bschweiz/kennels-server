from models import location


class Employee():
    
    def __init__(self, id, name, locationId, address):
        self.id = id
        self.name = name
        self.locationId = locationId
        self.address = address