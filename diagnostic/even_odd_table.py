# print numbers from 1 up until MAX_NUMBER, inclusive
MAX_NUMBER = 100

def main():
    for i in range(MAX_NUMBER):
        if i % 2 == 1:
            print(i, " is odd")
        else:
            print(i, " is even")

if __name__ == "__main__":
    main()