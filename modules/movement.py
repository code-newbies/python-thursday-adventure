# movement.py
"""This module handles code having to do with changes in location"""


def adjacent_tile(direction, start_x, start_y):
    """Finds the tile next to another tile in a specific direction"""
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

def next_tile(start, end):
    """given a starting and ending tile, this function will calculate the
    next tile to travel to along that route"""
    start_x, start_y = start
    #print("next_tile")
    #print(end)
    #print(end.coords)
    end_x, end_y = end.coords

    x_diff = start_x - end_x
    y_diff = start_y - end_y

    if x_diff == 0 and y_diff == 0:
        return end.coords

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

def what_direction(start, end):
    """This function determines the cardinal direction from one tile to
    an adjacent tile"""
    start_x, start_y = start
    #print("what_direction")
    #print(end)
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

def next_direction(start, end):
    """This function determines the cardinal directions to travel in to
    get to the next tile"""
    tile = next_tile(start, end)
    return what_direction(start, tile)

