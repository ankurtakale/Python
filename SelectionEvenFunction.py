def CheckEven(No):
    if (No % 2 == 0):
        print("It is even")
    else:
        print("It is odd")

def main():
    CheckEven(21)           # Positional arg
    CheckEven(No = 22)      # Keyword arg

if __name__ == "__main__":
    main()