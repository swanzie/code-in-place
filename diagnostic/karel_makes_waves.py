from karel.stanfordkarel import *

def main():
    for i in range(3):
        make_wave()
        move_to_next_wave()
    mave_wave()
    
def make_wave():
    """
    pre: karel is in row 1 facing east
    post: karel is one column over in row 1 facing east
    """
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    turn_around()
    move()
    move()
    turn_left()

def move_to_next_wave():
    """
    pre: karel is in row 1 facing east
    post: karel is in row 1 facing east
    """
    move()
    move()

# There is no need to edit code beyond this point

def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()


if __name__ == "__main__":
    run_karel_program()