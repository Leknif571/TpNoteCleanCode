import unittest
from src.model.parking import Parking
from src.model.place import Place 
from src.service.parking_service import ParkingService
from src.service.parking_service import ParkingEmptyException
from src.service.parking_service import PlaceNotFoundException
from parameterized import parameterized


class TestClassParking_Service_Unit(unittest.TestCase):

    def setUp(self):
        self._parking = Parking(0)
        self._parking_service = ParkingService(self._parking)


    def test_nothing(self):
        pass

    def test_create_parking_with_empty_place_return_true (self):
        self.assertTrue(self._parking_service.is_empty())

    def test_add_place_return_false(self):
        place1 = Place(1, True)
        self._parking_service.add_place(place1)
        self.assertFalse(self._parking_service.is_empty())

    def test_add_place_and_delete_place_return_true(self):
        place1 = Place(1, True)
        self._parking_service.add_place(place1)
        self._parking_service.delete_place(place1)
        self.assertTrue(self._parking_service.is_empty())

    def test_add_two_place_and_delete_one_return_false(self):
        place1 = Place(1, True)
        place2 = Place(2, True)
        self._parking_service.add_place(place1)
        self._parking_service.add_place(place2)
        self._parking_service.delete_place(place2)
        self.assertFalse(self._parking_service.is_empty())

    def test_delete_when_is_empty_return_empty_parking_exception(self):
         with self.assertRaises(ParkingEmptyException):
            self._parking_service.delete_place(Place(1, True))


    # @parameterized(
    #         Place(1, True),
    #         Place(2, True),
    #         Place(3, True),
    # )
    # def test_get_place_by_id_return_place(self, place):
    #     self._parking_service.add_place(place)
    #     self.assertEqual(place, self._parking_service.get_place_by_id(place.id))


    # @parameterized(
    #         Place(1, True),
    #         Place(2, True),
    #         Place(3, True),
    # )
    # def test_verify_place_not_exist_return_exception(self,place):
    #     with self.assertRaises(PlaceNotFoundException):
    #         self.assertEqual(place, self._parking_service.get_place_by_id(place.id))








if __name__ == '__main__':
    unittest.main()