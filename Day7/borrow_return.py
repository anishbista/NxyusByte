import datetime
import book_management, member_management

transaction_record = []


def check_book_availability(isbn):
    for i, item in enumerate(book_management.books.values(), 1):
        print(f"{i}. {item.display()}")
    if isbn in book_management.books and book_management.books[isbn].quantity > 0:
        print(f"{isbn} book is available")

    else:
        raise ValueError("Book not found")


def borrow_book(member_id, isbn):
    if isbn in book_management.books and member_id in member_management.members:
        if book_management.books[isbn].quantity > 0:
            book_management.books[isbn].quantity -= 1
            transaction_record.append(
                {
                    "transaction_type": "Borrowing",
                    "member_id": member_id,
                    "ISBN": isbn,
                    "borrow_date": datetime.datetime.now(),
                }
            )
            print(transaction_record)
        else:
            raise ValueError("Book is not available")
            # borrowing_record[isbn] = {"member_id":member_id,
            #     "ISBN":isbn,
            #     "borrow_date":datetime.datetime.now()}
    else:
        raise ValueError("Book or Member not found")


def return_book(member_id, isbn):
    for transaction in transaction_record:
        if transaction["member_id"] == member_id and transaction["ISBN"] == isbn:
            book_management.books[isbn].quantity += 1
            transaction_record.append(
                {
                    "transaction_type": "Returning",
                    "member_id": member_id,
                    "ISBN": isbn,
                    "return_date": datetime.datetime.now(),
                }
            )
            break

        else:
            raise ValueError("Member or ISBN record in transaction report not found")
