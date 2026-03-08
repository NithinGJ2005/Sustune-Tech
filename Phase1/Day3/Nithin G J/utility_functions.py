# Day 3: Utility Functions Module
# This module contains 7 reusable utility functions


# FUNCTION 1: CALCULATOR
def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operator (+, -, *, / only)"


# FUNCTION 2: STRING REVERSER
def reverse_string(text):
    return text[::-1]


# FUNCTION 3: PALINDROME CHECKER
def is_palindrome(text):
    return text == text[::-1]


# FUNCTION 4: FACTORIAL
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


# FUNCTION 5: LIST STATISTICS
def list_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total, average, maximum, minimum


# FUNCTION 6: EVEN FILTER
def filter_even(numbers):
    return [num for num in numbers if num % 2 == 0]


# FUNCTION 7: PASSWORD VALIDATOR
def validate_password(password):
    if len(password) < 8:
        return False

    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)

    return has_digit and has_upper and has_lower


# Testing the module (No keyboard input required)
if __name__ == "__main__":
    print("Calculator:", calculator(10, 5, "+"))
    print("Reverse String:", reverse_string("hello"))
    print("Is Palindrome:", is_palindrome("madam"))
    print("Factorial:", factorial(5))
    print("List Stats:", list_stats([10, 20, 30, 40, 50]))
    print("Even Numbers:", filter_even([1, 2, 3, 4, 5, 6]))
    print("Password Valid:", validate_password("Password123"))