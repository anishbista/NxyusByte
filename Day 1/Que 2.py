# Write a program that takes two numbers as input and finds out the GCD (greatest
# common divisor) of the two numbers using the Euclidean algorithm.

f_number = int(input("Enter the first positive number: "))
s_number = int(input("Enter the second positive number: "))

big_number = max(f_number, s_number)
small_number = min(f_number, s_number)

while small_number != 0:
    temp = small_number
    small_number = big_number % temp
    big_number = temp
    # big_number, small_number = small_number, big_number % small_number

print(f"GCD of {f_number} and {s_number} is {big_number}")
