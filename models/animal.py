
# let's define a class
class Animal():
    # class initializer, 5 params
    # DON'T FORGET the SELF
    def __init__(self, id, name, species, status, location_id, customer_id):
        self.id = id
        self.name = name
        self.species = species
        self.status = status
        self.location_id = location_id
        self.customer_id = customer_id