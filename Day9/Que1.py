import re


class User:
    def __init__(self):
        self.users = {}

    def validate_password(self, password):
        if re.match(
            r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@$%&*?])[A-Za-z\d@$!%*?&]{8,}$",
            password,
        ):
            return True

    def register_user(self, username, password):
        if self.validate_password(password):
            self.users[username] = password
            print(f"User '{username}' registered successfully!")
        else:
            print( 
                "Password should contain at least one lowercase,uppercase,digit and special characters and at least  8 characters"
            )


print("Commands\n 1.add-> To add new users\n 2.exit-> To exit the system")
account_manager = User()
while True:
    command = input("Enter the command: ")
    match command:
        case "add":
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            account_manager.register_user(username, password)
        case "exit":
            break
        case _:
            print("Invalid Command!")

print(account_manager.users)
