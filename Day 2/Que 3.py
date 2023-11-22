# Develop a Python program for managing books in a library with the following
# functionalities:
# 3.1 Book Inventory: Initialise an empty list to represent the library's book
# inventory.
# 3.2 Help Message: Display a help message to the user explaining the available
# commands:
# add -> add a book to the inventory
# remove -> remove a book from the inventory
# display -> display the current books in the inventory
# exit -> exit the program
# 3.3 Book Addition: Implement the ability to add a book to the inventory. When
# the user enters the add command, prompt them to enter the book title and
# author. Ensure that the same book cannot be added twice.
# 3.4 Book Removal: Implement the ability to remove a book from the
# inventory. When the user enters the remove command, prompt them to enter
# the title of the book they want to remove. Display an appropriate message if
# the book is not found in the inventory.
# 3.5 Inventory Display: Implement the display command to show the current
# books in the inventory. Display a message if the inventory is empty.
# 3.6 Exit Confirmation: When the user enters exit, prompt them with "Are you
# sure you want to exit?" If the user inputs "yes," the program should stop. If the
# user inputs anything else, the program should continue.

books = []
print(
    "Welcome to the Library Management. Here are commands that can be used to manage book \n add -> add a book to the inventory \n remove -> remove a book from the inventory \n display -> display the current books in the inventory \n exit -> exit the program"
)

while True:
    command = input("Enter the command: ")
    if command.lower() == "add":
        title = input("Enter the title of book to add: ")
        if title not in books:
            books.append(title)
        else:
            print("This book is already in list")
    elif command.lower() == "remove":
        title = input("Enter the title of book to delete: ")
        if title not in books:
            print(f"{title} book doesn't exist")
        else:
            books.remove(title)

    elif command.lower() == "display":
        print(f"Books in the library are {books}")

    elif command.lower() == "exit":
        choice = input("Are you sure you want to exit? ")
        if choice.lower() == "yes":
            print("Exiting the program")
            break
    else:
        print("Please enter a valid command(add/remove/display/exit)")
