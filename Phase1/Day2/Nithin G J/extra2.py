# This program prints numbers from 1 to 50.
# For multiples of 3, it prints "Fizz".
# For multiples of 5, it prints "Buzz".
# For multiples of both 3 and 5, it prints "FizzBuzz".

for num in range(1, 51):
    
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
