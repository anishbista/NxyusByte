# Question 2: Create a guessing game where the user has to guess a number between 1 and 100. Use a loop to give the user 3 attempts, and provide hints (higher/lower) based on their guesses until they get it right.
import random

right_number = random.randrange(0, 100)
# for x in range(3):
#     user_input = int(input("Enter any number between 1 and 100:"))
#     if user_input == right_number:
#         print("You guessed the number right")
#         break
#     elif user_input > right_number:
#         print("Your guessed number is higher than right number")
#     else:
#         print("Your guessed number is lower than right number")
# print("Right number is " + str(right_number))


attempts = 3

while attempts > 0:
    user_input = int(input("Enter any number between 1 and 100:"))
    if user_input == right_number:
        print("You guessed the number right")
        break
    elif user_input > right_number:
        print("Your guessed number is higher than right number")
    else:
        print("Your guessed number is lower than right number")

    attempts -= 1

    if attempts == 0:
        choice = input(
            "You've run out of attempts! Do you want to continue? (yes/no): "
        )
        if choice.lower() == "yes":
            attempts = 3
        else:
            print(f"The right number is {right_number}")
            break
