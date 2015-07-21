from uuid import uuid4

class Cockroach:
    def __init__(self, start_x, start_y):
        self.name = "cockroach"
        self.start_x = start_x
        self.start_y = start_y
        self.uid = uuid4()

    def init(self, level):
        level.add_item(self.name, self.start_x, self.start_y)
