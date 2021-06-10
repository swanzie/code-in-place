"""
TODO: Write a description here
"""

import random
TARGET_ROUNDS_CORRECT = 3 #the number of rounds you want the user to get correct

def main():
    rounds_correct = 0 #how many rounds the user has gotten correct
    user_correct = False

    while rounds_correct < TARGET_ROUNDS_CORRECT:
        user_correct = one_round(rounds_correct)
        if user_correct:
            rounds_correct +=1
        else:
            rounds_correct = 0
    print("Congratulations! You mastered addition.")

def one_round(num_correct):
    #generate two numbers
    num1 = random.randint(10,100)
    num2 = random.randint(10,100)

    #ask user for their answer
    print("What is " + str(num1) + " + " + str(num2) + "?")
    user_response = input("Your answer: ")
    user_response = int(user_response)

    #evaluate correctness
    correct = num1 + num2
    if correct == user_response:
        print("Correct! You've gotten " + str(num_correct+1) + " in a row.")
        return True
    else:
        print("Incorrect. The expected answer is " + str(correct))
        return False

if __name__ == '__main__':
    main()