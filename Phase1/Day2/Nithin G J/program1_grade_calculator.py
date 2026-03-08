# This program takes marks (0–100) as input from the user
# and assigns a grade (A, B, C, F) using if/elif/else conditions.

marks = float(input("Enter your marks (0 - 100): "))

if 100 >= marks >= 90:
    print("Grade A")
elif 89 >= marks >= 75:
    print("Grade B")
elif 74 >= marks >= 50:
    print("Grade C")
elif marks < 50:
    print("Grade F")
else:
    print("Invalid marks! Please enter marks between 0 and 100.")
