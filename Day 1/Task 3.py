# Question 3: Write a program that takes N numbers as input from a user and puts them in a list. Then the program should find out the sum of all the odd numbers and the sum of all the even numbers from the list and print them out.

n = int(input("Enter the number of elements: "))
number = []
for i in range(n):
    num = int(input(f"Enter number {i + 1}:"))
    number.append(num)


odd = 0
even = 0

for num in number:
    if num % 2 == 0:
        even += num
    else:
        odd += num

print(f"Sum of odd numbers:{odd}")
print(f"Sum of even numbers:{even}")
