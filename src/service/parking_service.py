from src.model.parking import Parking
from src.model.place import Place


class ParkingService():
    def __init__(self, parking: Parking):
        
        self.parking = parking

    def is_empty(self):
        return len(self.parking.places) == 0
    
    def add_place(self, place):
        self.parking.places.append(place)
   
    def delete_place(self, place):
        if self.is_empty() == True :
            raise ParkingEmptyException("Il n'y aucune place qui peut être supprimer")
        self.parking.places.remove(place)

    def get_place_by_id(self, place : Place):
        if self.parking.get_place_by_id(place.id) == None :
            raise PlaceNotFoundException
        return self.parking.get_place_by_id(place.id);


class ParkingEmptyException(Exception):
    pass

class PlaceNotFoundException(Exception):
    pass