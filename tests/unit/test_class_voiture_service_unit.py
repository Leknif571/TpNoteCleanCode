import unittest
from src.service.voiture_service import VoitureService
from src.model.voiture import Voiture


class TestClassVoitureServiceUnit(unittest.TestCase):


    def test_nothing(self):
        pass

    def test_verify_voiture_are_parked(self):
        voiture_service = VoitureService()
        voiture = Voiture("ABC123", True)
        self.assertTrue(voiture_service.is_parked(voiture))

    def test_verify_place_are_not_parked(self):
        voiture_service = VoitureService()
        voiture = Voiture("ABC123", False)
        self.assertFalse(voiture_service.is_parked(voiture))

    


if __name__ == '__main__':
    unittest.main()