import unittest
import time
from src.model.parking import Parking
from src.model.place import Place
from src.service.parking_service import ParkingService

class TestPerformance(unittest.TestCase):

    def test_add_place_performance():
        parking = Parking(places=[])
        service = ParkingService(parking=parking)
        place = Place(id=1, name="Place 1")

        start_time_add = time.time()
        service.add_place(place)
        end_time_add = time.time()
        
        add_time = end_time_add - start_time_add

        assert add_time < 0.1, f"Le temps pour ajouter une place ({add_time:.6f}s) dépasse le seuil de {0.1}s"

    def test_delete_place_performance():
        parking = Parking(places=[])
        service = ParkingService(parking=parking)
        
        place = Place(id=1, name="Place 1")
        service.add_place(place)  

        start_time_delete = time.time()
        service.delete_place(place)
        end_time_delete = time.time()
        
        delete_time = end_time_delete - start_time_delete
        print(f"Temps pour supprimer une place : {delete_time:.6f} secondes")

        assert delete_time < 0.1, f"Le temps pour supprimer une place ({delete_time:.6f}s) dépasse le seuil de {0.1}s"

# if __name__ == "__main__":
#     test_add_place_performance()
#     test_delete_place_performance()

if __name__ == '__main__':
    unittest.main()