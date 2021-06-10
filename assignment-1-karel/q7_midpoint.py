from karel.stanfordkarel import *

"""
File: Midpoint.py
------------------------
Place a beeper in the middle of the first row.
"""

def main():
    """
    Karel will find the middle corner to place a beeper
    """
    paint_to_middle()
    place_middle_beeper()
    clear_colors()
    find_beeper()

def find_beeper():
    """
    pre: Karel is at left or right edge of world, facing out
    post: Karel is on beeper
    """
    turn_around()
    while no_beepers_present():
        move()

def paint_to_middle():
    """
    pre: Karel is on bottom row, bottom row has no beepers, and all corners are blank
    post: Karel one corner off of middle, bottom row has no beepers, all corners are colored
    """
    paint_boundary_corners()
    while corner_color_is(BLANK):
        paint_color_two()
        paint_color_one()

def paint_boundary_corners():
    """
    pre: Karel is at (1,1), facing east, all corners are blank
    post: Karel is at (2,1), facing east, most west and most east corners are green
    """
    for i in range(2):
        while front_is_clear():
            if corner_color_is(BLANK):
                move()
        paint_corner(GREEN)
        turn_around()
        if front_is_clear():
            move()

def paint_color_one():
    """
    pre: Karel is next to a pink corner facing towards the center
    post: Karel is next to a pink corner facing towards the center
    """
    for i in range(2):
        while corner_color_is(BLANK):
            move()
        if corner_color_is(PINK):
            turn_around()
            move()
            paint_corner(GREEN)
            move()

#find the next blank corner and paint pink
def paint_color_two():
    """
    pre: Karel is next to green corner, facing towards the center
    post: Karel is next to a green corner, facing towards the center
    """
    for i in range(2):
        while corner_color_is(BLANK):
            move()
        if corner_color_is(GREEN):
            turn_around()
            move()
            paint_corner(PINK)
            move()

def turn_around():
    for i in range(2):
        turn_left()

def clear_colors():
    """
    pre: none
    post: all corners are Blank and Karel is at edge of row, facing out toward boundary
    """
    move_to_boundary()
    while front_is_clear():
        paint_corner(BLANK)
        move()
    paint_corner(BLANK)

def move_to_boundary():
    """
    pre: none
    post: Karel is at edge of row facing away from boundary
    """
    while front_is_clear():
        move()
    turn_around()

def place_middle_beeper():
    """
    pre: Karel is next to middle corner
    post: Karel is on middle corner and beeper is placed on middle corner
    """
    turn_around()
    if front_is_clear():
        move()
    put_beeper()

if __name__ == '__main__':
    run_karel_program('Midpoint.w')