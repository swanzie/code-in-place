from karel.stanfordkarel import *

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        #pre: karel is facing east and hasn't reached end of world
        #post: karel is facing east and has placed a beeper
        place_next_beeper()
        move_to_next_corner()
    put_beeper()

def place_next_beeper():
    put_beeper()

def move_to_next_corner():
    #pre: karel is facing east and hasn't reached end of world
    #post: karel is facing east and is one row higher, and at the corner to place next beeper
    for i in range(2):
        move()
    turn_left()
    move()
    turn_right()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    run_karel_program('RampKarel3.w')