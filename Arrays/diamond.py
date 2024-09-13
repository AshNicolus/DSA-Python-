def nStarDiamond(n: int) -> None:
    # Upper part of the diamond
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        # Print stars
        for k in range(2 * i - 1):
            print("*", end="")
        print()  # Move to the next line after each row

    # Lower part of the diamond
    for i in range(n - 1, 0, -1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        # Print stars
        for k in range(2 * i - 1):
            print("*", end="")
        print()  # Move to the next line after each row

n = int(input("Write no. :"))