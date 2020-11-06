"""
Write a program that generates two integers under 100 and
prompts the user to enter the sum of these two integers. The program then reports
true if the answer is correct, false otherwise.
"""
import random

# Generate two integers
number1 = random.randint(0, 100)
number2 = random.randint(0, 100)

# prompts the user to enter the sum of these two integers
guess_sum = eval(input(f"{number1} + {number2} = "))

if number1 + number2 == guess_sum:
    print(f"The answer is True")
    print(f"{number1} + {number2} = {number1 + number2}")
else:
    print("The answer is False")
    print(f"{number1} + {number2} != {guess_sum}")
