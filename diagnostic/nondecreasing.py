def main():
    # ask user for sequence of non-decreasing numbers and track the sequence length
    intro_message()
    sequence_length = user_playing()
    exit_message(sequence_length)

def user_playing():
    first_num = float(input("Enter num: "))
    second_num = float(input("Enter num: "))
    sequence_length = 1

    while first_num <= second_num:
        first_num = second_num
        second_num = float(input("Enter num: "))
        sequence_length += 1

    return sequence_length

def intro_messeage():
    print("Enter a sequence of non-decreasing numbers.")

def exit_message(sequence_length):
    print("Thanks for playing!")
    print("Sequence length: ", sequence_length)

if __name__ == "__main__":
    main()