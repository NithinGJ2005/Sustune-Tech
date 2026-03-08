# This program takes a starting number from the user
# and counts down to 0 using a while loop.
# After reaching 0, it prints "Liftoff!".

num = int(input("Enter the starting number: "))

while num >= 0:
    print(num)
    num -= 1

print("Liftoff!")
