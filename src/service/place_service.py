from src.model.place import Place

class PlaceService:
    def __init__(self, place : Place):
        self.is_available = place

    def is_available(self):
        return self.is_available