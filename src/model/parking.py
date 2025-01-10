class Parking():
    def __init__(self, id):
        self.id = id
        self.places = []

    def get_place_by_id(self, id):
        for place in self.places:
            if place.id == id:
                return place
        return None
    
    def get_places(self):
        return self.places



