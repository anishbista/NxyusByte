import datetime, os
import book_management, member_management, borrow_return


def generate_book_inventory_report():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"book_inventory_report_{timestamp}.txt"

    with open(filename, "w") as file:
        file.write("Current Book Inventory:\n")
        for book in book_management.books.values():
            file.write(book.display() + "\n")

    print(f"Book Inventory Report generated: {filename}")


def generate_member_borrowing_report():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"member_borrowing_report_{timestamp}.txt"

    with open(filename, "w") as file:
        file.write("Member Borrowing Report:\n")
        for record in borrow_return.transaction_record:
            if record["transaction_type"] == "Borrowing":
                file.write(
                    f"Transaction Type='Borrow' - Member ID: {record['member_id']} - ISBN: {record['ISBN']} - Borrow Date: {record['borrow_date']}\n"
                )
            else:
                file.write(
                    f"Transaction Type='Return' - Member ID: {record['member_id']} - ISBN: {record['ISBN']} - Return Date: {record['return_date']}\n"
                )

    print(f"Member Borrowing Report generated: {filename}")


def calculate_fine(isbn, return_date):
    if isbn in borrow_return.transaction_record:
        due_date = borrow_return.transaction_record[isbn]["borrow_date"]
        days_overdue = (return_date - due_date).days
        if days_overdue > 0:
            # Assuming a fixed fine rate per day for overdue books
            fine_rate_per_day = 2  # Change this to your desired fine rate
            fine = days_overdue * fine_rate_per_day
            return fine
    return 0  # If not overdue or not found in records, no fine is applicable
