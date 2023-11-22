# 3. Create a program for "Car Racing" with the following functionalities:
# a. The initial state of the car is in the "stop" state.
# b. Display a help message to the user explaining the available commands:
# start -> start the car
# stop -> stop the car
# exit -> exit the program
# c. Users are not allowed to enter the same command if the car is already in the
# same state. For example:
# If the car is in the "start" state and the user enters the start command
# again, display "Car is already in start state."
# Similarly, if the car is in the "stop" state and the user enters the stop
# command again, display "Car is already in stop state."
# d. When the user enters exit, prompt them with "Are you sure you want to exit?"
# If the user inputs "yes," the program should stop. If the user inputs anything
# else, the program should continue.

print(
    "Welcome to the Car Racing game.\nCommand for game:\nstart -> start the car \nstop -> stop the car \nexit -> exit the program "
)
state = "stop"
while True:
    user_input = input("Enter the command: ")
    if user_input.lower() == state:
        print(f"Car is already in {state} state")
    elif user_input.lower() == "exit":
        choice = input("Are you sure you want to exit?: ")
        if choice.lower() == "yes":
            print("Exiting the game")
            break
    elif user_input.lower() == "start" or user_input.lower() == "stop":
        state = user_input.lower()
    else:
        print("Please enter a valid command (start/stop/exit)")
