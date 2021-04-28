from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""

def main():
    """
    Karel will pick up the last puzzle piece
    Karel will place the last puzzle piece
    Karel will return to her original position
    """
    last_puzzle()
    place_last_piece()
    return_karel()

def last_puzzle():
    move()
    move()
    pick_beeper()

def place_last_piece():
    move()
    turn_left()
    move()
    move()
    put_beeper()

def return_karel():
    turn_around()
    move()
    move()
    turn_right()
    move()
    move()
    move()
    turn_around()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    run_karel_program('Puzzle.w')