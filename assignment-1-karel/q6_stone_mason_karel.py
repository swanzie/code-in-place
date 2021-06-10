from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter code.
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        repair_column()
        move_to_next_column()
    #final repair
    repair_column()

def move_to_next_column():
    #pre: karel facing east at row 1 of one column
    #post: karel facing east at row 1 at next column, four avenues apart
    for i in range(4):
        move()

def repair_column():
    #pre: karel facing east and at row 1
    #post: karel facing east and at row 1 after column repaired
    turn_left()
    #karel repairing column
    while front_is_clear():
        safe_place()
        move()
    safe_place()
    return_to_bottom()

def turn_around():
    for i in range(2):
        turn_left()

def return_to_bottom():
    #pre: karel facing north at top of column
    #post: karel facing east at bottom of column
    turn_around()
    while front_is_clear():
        move()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()

def safe_place():
    if no_beepers_present():
        put_beeper()

if __name__ == '__main__':
    run_karel_program('SampleQuad2.w')