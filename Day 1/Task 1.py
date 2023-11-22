import random

# Question 1: Write a programs that takes a number as input from the user and prints all the even numbers up to that number using a loop and conditional statement.

# number = int(input("Enter any number: "))
# for num in range(number + 1):
#     if num % 2 == 0:
#         print(num)

# Question 2: Create a guessing game where the user has to guess a number between 1 and 100. Use a loop to give the user 3 attempts, and provide hints (higher/lower) based on their guesses until they get it right.

right_number = random.randrange(0, 100)
for x in range(3):
    user_input = int(input("Enter any number between 1 and 100:"))
    if user_input == right_number:
        print("You guessed the number right")
    elif user_input > right_number:
        print("Your guessed number is higher than right number")
    else:
        print("Your guessed number is lower than right number")

print("Right number is" + right_number)


# Question 3: Write a program that takes N numbers as input from a user and puts them in a list. Then the program should find out the sum of all the odd numbers and the sum of all the even numbers from the list and print them out.


# Question 4: Develop a program that takes a sentence from the user and counts the number of vowels in it using a loop and conditional statement.

# Question 5: Design a simple calculator that asks the user for two numbers and an operation (addition, subtraction, multiplication, division) and performs the calculation using conditional statements and user input.
