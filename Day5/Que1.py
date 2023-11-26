class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def __str__(self):
        return f" Roll Number:{self.roll_number} Name:{self.name} Marks:{self.marks}"


students = []


def add_students():
    try:
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        for student in students:
            if student.roll_number == roll_number:
                print("Roll number already exists.")
                return
        marks = float(input("Enter marks: "))
        new_student = Student(name, roll_number, marks)
        students.append(new_student)
        print("Successfully added")
    except ValueError:
        print("Invalid ! Please enter a numeric value.")


def view_student():
    if not students:
        print("Students not found!")
    else:
        sorted_student = sorted(students, key=lambda x: x.marks)
        for student in sorted_student:
            print(student)


def search_student():
    roll = input("Enter roll number: ")
    for student in students:
        if student.roll_number == roll:
            print(student)
            return
    print("Student not found.")


def update_student():
    roll = input("Enter roll number to update: ")
    for student in students:
        if student.roll_number == roll:
            try:
                name = input("Enter new name: ")
                marks = float(input("Enter new marks:  "))
                student.name = name
                student.marks = marks
                return
            except ValueError:
                print("Invalid input!")
    print("Student not found. ")


def delete_student():
    roll = input("Enter roll number to delete: ")
    for student in students:
        if student.roll_number == roll:
            students.remove(student)
            return
    print("Students not found.")


print(
    "Commands for Student Management System\n add-> Add Students\n view-> View All Students\n search-> Search Student\n update-> Update Student Information\n delete-> Delete Student\n exit-> Exit"
)
while True:
    command = input("Enter the commands: ").lower()

    match command:
        case "add":
            add_students()
        case "view":
            view_student()
        case "search":
            search_student()
        case "update":
            update_student()
        case "delete":
            delete_student()
        case "exit":
            print("Exiting the program.......")
            break
        case "help":
            print(
                "Commands for Student Management System\n add-> Add Students\n view-> View All Students\n search-> Search Student\n update-> Update Student Information\n delete-> Delete Student\n exit-> Exit"
            )
        case _:
            print("Invalid Command! ")
