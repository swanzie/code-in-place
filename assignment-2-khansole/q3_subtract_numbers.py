"""
Asks the user for two numbers and prints the result
of the first number minus the second number.
"""

def main():
    print("This program subtracts one number from another.")
    num1 = input("Enter first number: ")
    num1 = float(num1)
    num2 = input("Enter second number: ")
    num2 = float(num2)
    result = num1 - num2
    print("The result is " + str(result))

if __name__ == '__main__':
    main()