# Question 5: Design a simple calculator that asks the user for two numbers and an operation (addition, subtraction, multiplication, division) and performs the calculation using conditional statements and user input.


f_number = float(input("Enter the first number: "))
s_number = float(input("Enter the second number: "))
operation = input("Enter operation (+, -, *, /): ")

result = 0

if operation == "+":
    result = f_number + s_number
elif operation == "-":
    result = f_number - s_number
elif operation == "*":
    result = f_number * s_number
else:
    result = f_number / s_number

print(f"{operation} between two numbers is {result}")
