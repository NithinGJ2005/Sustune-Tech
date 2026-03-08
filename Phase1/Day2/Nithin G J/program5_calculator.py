# This program takes two numbers and an operation (+, -, *, /)
# from the user and performs the selected calculation.
# It also checks for division by zero.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    print("Result:", num1 + num2)

elif operation == "-":
    print("Result:", num1 - num2)

elif operation == "*":
    print("Result:", num1 * num2)

elif operation == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero")
    else:
        print("Result:", num1 / num2)

else:
    print("Invalid operation selected")
