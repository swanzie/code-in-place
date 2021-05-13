"""
Part A:
function divide_and_round() does not have a return statement so in the main function
so it'll print 10, which was the original value assigned to n
"""

"""
Part B: 
Edit this code so that it works correctly
"""

def divide_and_round(n):
    """
    Divides an integer n by 2 and rounds 
    up to the nearest whole number
    """
    if n % 2 == 0:
        n = n / 2
    else:
        n = (n + 1) / 2
    return n

def main():
    n = 10
    print(divide_and_round(n)) 