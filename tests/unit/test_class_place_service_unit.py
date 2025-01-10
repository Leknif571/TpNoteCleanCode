import unittest
from src.service.place_service import PlaceService
from src.model.place import Place


class TestClassPlaceServiceUnit(unittest.TestCase):

    def test_nothing(self):
        pass

    def test_verify_place_are_available(self):
        place_service = PlaceService()
        place = Place(0, True)
        self.assertTrue(place_service.is_available(place))


    def test_verify_place_are_not_available(self):
        place_service = PlaceService()
        place = Place(1, False)
        self.assertFalse(place_service.is_available(place))

    def test_verify_place_are_again_available(self):
        place_service = PlaceService()
        place = Place(1, True)
        self.assertTrue(place_service.is_available(place))
        place.set_is_not_available()
        self.assertFalse(place_service.is_available(place))
        


if __name__ == '__main__':
    unittest.main()