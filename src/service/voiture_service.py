from src.model.voiture import Voiture

class VoitureService:
    def __init__(self, voiture : Voiture):
        self.is_parked = voiture

    def is_parked(self, car_id):
        return self.is_parked