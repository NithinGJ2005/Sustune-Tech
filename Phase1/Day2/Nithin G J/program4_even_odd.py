# This program asks the user to enter 5 numbers.
# It checks each number and prints whether it is even or odd.

for i in range(5):
    number = int(input("Enter a number: "))
    
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
print("bye")
