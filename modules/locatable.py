from uuid import uuid4

class Locatable:
    def __init__(self):
        self.uid = uuid4()
        self.coords = (0, 0)
        self.display = "!"

    def place(self, coords):
        self.coords = coords

    def set_display(self, display):
        self.display = display

    def is_at(self, coords):
        return self.coords == coords

    def locate(self):
        return self.coords

    def go(self, direction):
        if direction == "n":
            self.coords = (self.coords[0], self.coords[1] + 1)
        elif direction == "s":
            self.coords = (self.coords[0], self.coords[1] - 1)
        elif direction == "e":
            self.coords = (self.coords[0] + 1, self.coords[1])
        elif direction == "w":
            self.coords = (self.coords[0] - 1, self.coords[1])
