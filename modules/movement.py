
class Movement:
    def adjacent_tile(self, direction, start_x, start_y):
        if direction == "n":
            return (start_x, start_y + 1)
        elif direction == "s":
            return (start_x, start_y - 1)
        elif direction == "e":
            return (start_x + 1, start_y)
        elif direction == "w":
            return (start_x - 1, start_y)
        else:
            return (start_x, start_y)
