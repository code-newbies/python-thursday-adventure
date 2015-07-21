
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

    def next_tile(self, start, end):
        start_x, start_y = start
        end_x, end_y = end   

        x_diff = start_x - end_x
        y_diff = start_y - end_y


        if x_diff == 0 and y_diff == 0:
            return end  

        if abs(x_diff) > abs(y_diff):
            if x_diff > 0:
                return (start_x - 1, start_y)
            else:
                return (start_x + 1, start_y)
        else:
            if y_diff > 0:
                return (start_x, start_y - 1)
            else:
                return (start_x, start_y + 1)

    def next_direction(self, start, end):
        tile = self.next_tile(start, end)
        return self.what_direction(start, tile)

    def what_direction(self, start, end):
        start_x, start_y = start
        end_x, end_y = end   

        x_diff = start_x - end_x
        y_diff = start_y - end_y

        if x_diff == 0 and y_diff == 0:
            return None 

        if y_diff > 0:
            return "s"
        elif y_diff < 0:
            return "n"
        elif x_diff > 0:
            return "w"
        else:
            return "e"
