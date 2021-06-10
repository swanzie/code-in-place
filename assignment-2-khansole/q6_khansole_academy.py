"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random 

def main():
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
        print("Correct!")
    else:
        print("Incorrect. The expected answer is " + str(correct))

if __name__ == '__main__':
    main()