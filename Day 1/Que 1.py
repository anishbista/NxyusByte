# 1. The factorial of a non-negative integer N, denoted by N!, is the product of all positive
# integers less than or equal to N.
# 5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input("Enter non-negative integer: "))

if n < 0:
    print("Negative number doesn't have factorial")
else:
    factorial = 1
    for x in range(2, n + 1):
        factorial *= x

    print(f"Factorial of {n} is {factorial}")
