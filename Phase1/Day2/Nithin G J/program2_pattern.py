# This program asks the user for a number and prints a star pattern from 1 up to that number using a for loop.

num = int(input("Enter a number: "))

for i in range(1, num + 1):
    print("*" * i)
