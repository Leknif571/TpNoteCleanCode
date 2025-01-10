

class Place():
    def __init__(self, id, is_available):
        self.id = id
        self.is_available = is_available

    def set_is_available(self):
        self.is_available = True

    def set_is_not_available(self):
        self.is_available = False