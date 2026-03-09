# Day 3: Utility Functions Module (Improved with Error Handling)
# This module contains 7 reusable utility functions with
# proper validation and error handling.


# FUNCTION 1: CALCULATOR
# Performs basic arithmetic operations between two numbers.
# Supported operators: +, -, *, /
# Includes validation for data type, invalid operators and division by zero.

def calculator(num1, num2, operation):
    try:
        # Ensure both inputs are numbers (int or float)
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            return "Error: Numbers must be int or float"

        # Perform addition
        if operation == "+":
            return num1 + num2

        # Perform subtraction
        elif operation == "-":
            return num1 - num2

        # Perform multiplication
        elif operation == "*":
            return num1 * num2

        # Perform division with zero check
        elif operation == "/":
            if num2 == 0:
                return "Error: Cannot divide by zero"
            return num1 / num2

        # Handle invalid operator
        else:
            return "Error: Invalid operator. Use +, -, *, /"

    # Catch unexpected runtime errors
    except Exception as e:
        return f"Error: {e}"


# FUNCTION 2: STRING REVERSER
# Reverses a given string.
# Validates input type and handles None values.
def reverse_string(text):
    # Check for None input
    if text is None:
        return "Error: Input cannot be None"

    # Ensure input is a string
    if not isinstance(text, str):
        return "Error: Input must be a string"

    # Reverse string using slicing
    return text[::-1]


# FUNCTION 3: PALINDROME CHECKER
# Checks whether a string reads the same forward and backward.

def is_palindrome(text):
    # Validate input
    if text is None:
        return "Error: Input cannot be None"

    if not isinstance(text, str):
        return "Error: Input must be a string"

    # Compare string with its reverse
    return text == text[::-1]


# FUNCTION 4: FACTORIAL
# Calculates factorial of a non-negative integer.
# Includes validation for type, negative values, and size limit.
def factorial(n):
    # Ensure input is an whole-number
    if not isinstance(n, int):
        return "Error: Factorial only works for whole numbers"

    # Reject negative numbers
    if n < 0:
        return "Error: Negative numbers not allowed"

    # Prevent extremely large computations
    if n > 100:
        return "Error: Number too large"

    # Compute factorial using loop
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


# FUNCTION 5: LIST STATISTICS
# Returns total, average, maximum, and minimum
# from a list of numbers.
def list_stats(numbers):
    # Validate input type
    if not isinstance(numbers, list):
        return "Error: Input must be a list"

    # Ensure list is not empty
    if len(numbers) == 0:
        return "Error: Cannot calculate stats for empty lists"

    # Ensure all elements are numeric
    for item in numbers:
        if not isinstance(item, (int, float)):
            return "Error: All items must be numbers"

    # Calculate statistics
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total, average, maximum, minimum


# FUNCTION 6: EVEN FILTER
# Returns a new list containing only even integers
# from the input list.
def filter_even(numbers):
    # Validate input type
    if not isinstance(numbers, list):
        return "Error: Input must be a list"

    even_numbers = []

    # Check each element
    for num in numbers:
        if not isinstance(num, int):
            return "Error: List must contain only integers"

        # Append only even numbers
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers



# FUNCTION 7: PASSWORD VALIDATOR
# Validates password strength.
# Conditions:
# - Minimum 8 characters
# - At least one digit
# - At least one uppercase letter
# - At least one lowercase letter

def validate_password(password):
    # Check for None input
    if password is None:
        return "Error: Password cannot be None"

    # Ensure password is string
    if not isinstance(password, str):
        return "Error: Password must be a string"

    # Check for empty string
    if password == "":
        return "Error: Password cannot be empty"

    # Minimum length requirement
    if len(password) < 8:
        return False

    has_digit = False
    has_upper = False
    has_lower = False

    # Check character conditions
    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True

    return has_digit and has_upper and has_lower


# TEST SECTION
# Executes sample test cases when file is run directly.
if __name__ == "__main__":

    print("Calculator:")
    print(calculator(10, 5, '+'))
    print(calculator(10, 0, '/'))
    print(calculator(10, 5, '%'))

    print("\nString Reverser:")
    print(reverse_string("hello"))
    print(reverse_string(None))
    print(reverse_string(123))

    print("\nPalindrome:")
    print(is_palindrome("madam"))
    print(is_palindrome(None))
    print(is_palindrome(123))

    print("\nFactorial:")
    print(factorial(5))
    print(factorial(-5))
    print(factorial(3.5))
    print(factorial(200))

    print("\nList Stats:")
    print(list_stats([10, 20, 30]))
    print(list_stats([]))
    print(list_stats([1, 'hello', 3]))
    print(list_stats("not a list"))

    print("\nEven Filter:")
    print(filter_even([1, 2, 3, 4, 5]))
    print(filter_even("123"))
    print(filter_even([1, 'two', 3]))

    print("\nPassword Validator:")
    print(validate_password("Password123"))
    print(validate_password(None))
    print(validate_password(""))
    print(validate_password(12345))