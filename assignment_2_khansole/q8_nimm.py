"""
Program to simiulate game of Nimm
Game starts with 20 stones between players
2 players alternate taking 1 or 2 stones (asking user how many stones) until there are zero left
The player who takes the last stone loses
"""

import random

def main():
    player1 = True
    stones_remain = 20
    
    while stones_remain > 0:
        stones_remain = one_round(player1, stones_remain)
        if stones_remain <= 0:
            if player1:
                print("Player 2 wins!")
            else:
                print("Player 1 wins!")
        player1 = switch_player(player1)

#to change which player's turn it is
def switch_player(player1):
    if player1 == True:
        return False
    else:
        return True

#one round 
def one_round(player1, stones_remain):
    if player1:
        player = 1
    else:
        player = 2

    print("There are " + str(stones_remain) + " stones left")
    stones_to_remove = int(input("Player " + str(player) + " would you like to remove 1 or 2 stones? "))
    input_is_invalid = True
    
    while input_is_invalid:
        if stones_to_remove == 1 or stones_to_remove == 2:
            input_is_invalid = False
        # if user inputed an invalid option besides 1 or 2
        else:
            stones_to_remove = int(input("Please enter 1 or 2: "))
    print("")
    stones_remain -= stones_to_remove
    return stones_remain        

if __name__ == '__main__':
    main()