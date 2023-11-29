import book_management, borrow_return, member_management, report_generation


def add_book():
    isbn = int(input("Enter the ISBN: "))
    book_title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    quantity = int(input("Enter quantity of book: "))
    book_management.add_books(isbn, book_title, author, quantity)


def update_book():
    isbn = int(input("Enter the ISBN to update: "))
    book_title = input("Enter new Book Title: ")
    author = input("Enter new Author Name: ")
    quantity = int(input("Enter new quantity of book: "))
    book_management.update_books(isbn, book_title, author, quantity)


def remove_book():
    isbn = int(input("Enter the ISBN to remove: "))
    book_management.remove_books(isbn)


def add_member():
    member_id = int(input("Enter id for member: "))
    member_name = input("Enter name of member: ")
    phone_number = int(input("Enter phone no: "))
    member_management.add_member(member_id, member_name, phone_number)


def update_member():
    member_id = int(input("Enter id for member: "))
    member_name = input("Enter name of member: ")
    phone_number = int(input("Enter phone no: "))
    member_management.update_member(member_id, member_name, phone_number)


def remove_member():
    member_id = int(input("Enter member id: "))
    member_management.remove_member(member_id)


def check_book_availability():
    isbn = int(input("Enter isbn of book: "))
    borrow_return.check_book_availability(isbn)


def borrow_book():
    member_id = int(input("Enter member id: "))
    isbn = int(input("Enter isbn of book: "))
    borrow_return.borrow_book(member_id, isbn)


def return_books():
    member_id = int(input("Enter member id: "))
    isbn = int(input("Enter isbn of book: "))
    borrow_return.return_book(member_id, isbn)


print(
    "Options for Library Management:\n 1.Add Book\n 2.Update Book\n 3.Remove Book\n 4.Add Member\n 5.Update Member\n 6.Remove Member\n 7.Check Book Availability\n 8.Borrow Book\n 9.Return Book\n 10.Generate Book Inventory Report\n 11.Generate Member Borrowing Report"
)


while True:
    choice = input("Enter your choice: ")
    try:
        match choice:
            case "1":
                add_book()
            case "2":
                update_book()
            case "3":
                remove_book()
            case "4":
                add_member()
            case "5":
                update_member()
            case "6":
                remove_member()
            case "7":
                check_book_availability()
            case "8":
                borrow_book()
            case "9":
                return_books()
            case "10":
                report_generation.generate_book_inventory_report()
            case "11":
                report_generation.generate_member_borrowing_report()
            # case "8":
            #     print("Exiting the program.......")
            #     break
            # case "9":
            #     print(
            #         "Options:\n 1.Add Item\n 2.Remove Item\n 3.Update Item\n 4.View Inventory\n 5.Low Stock Report\n 6.Sort Inventory\n 7.Exit\n 8.Help"
            #     )
            case _:
                print("Invalid Command! ")
    except ValueError as e:
        print(f"Error: {e}")
