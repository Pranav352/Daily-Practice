#################### Exception Handling #####################
# try,except,else,finally,raise

try:
    x = 10/0
except ZeroDivisionError:
    print("cannot divide by zero")

try:
    num = int(input("Enter Number:"))
    result = 10/num
except ValueError:
    print("Invalid Input! Please enter an integer")
except ZeroDivisionError:
    print("cannot divide by zero")


try:
    print("hello")
except Exception:
    print("something went wrong")
else:
    print("no errors occured")



# Task 
# Challenge Task (Important for Exams)
# Create a simple calculator that:
# Takes two numbers
# Takes an operation (+ - * /)
# Handles:
# ValueError
# ZeroDivisionError
# Invalid operator

try:
    num1 = float(input("Enter first NUmbetr:"))
    num2 = float(input("Enter second number:"))
    operator = input("Enter operator(+,-,*,/):")

    if operator == "+":
        print("Result:",num1 + num2)
    elif operator == "-":
        print("Result:",num1 - num2)
    elif operator == "*":
        print("Result:",num1 * num2)
    elif operator == "/":
        print("Result:",num1 / num2)
    else:
        print("Invalid operator")
except ValueError:
    print("Error: Please Enter valid Numbers")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
    



