def main():
    """
    Ask for user's height and respond with whether the user is the correct height to be an astronaut
    """
    height = get_height()
    is_astronaut_height(height)

#ask user for height in meters
def get_height():
    height = input("Enter your height in meters: ")
    return height

#respond whether height is correct for astronaut
def is_astronaut_height(height):
    if height < 1.6:
        print("Below minimum astronaut height")
    elif height > 1.9:
        print("Above maximum astronaut height")
    else:
        print("Correct height to be an astronaut")

if __name__ == "__main__:
    main()