#  Write a program that prompts the user to enter a number. Create a list of squares of all numbers from 1 to the user-entered number.


def list_square(n):
    squares = []
    for x in range(1, n + 1):
        squares.append(x * x)
    return squares


n = int(input("Enter any number: "))
print(list_square(n))
