from uuid import uuid4

class Locatable:
    def __init__(self):
        self.uid = uuid4()
        self.coords = (0, 0)

    def place(self, coords):
        self.coords = coords
