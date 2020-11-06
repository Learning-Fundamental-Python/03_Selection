"""
generates two integers and prompts the user to enter the sum of these two integers.
Revise the program to generate three single-digit integers and prompt the user
to enter the sum of these three integers.
"""
import random

# Case 01
# Generate two numbers of integer
number1 = random.randint(0, 99)
number2 = random.randint(0, 99)

# Sum betwwen two integers
print(f"The sum of two integer, ({number1} + {number2}) is {number1 + number2}")

# Case 02
# generate three single-digit integers
number1 = random.randint(0, 99)
number2 = random.randint(0, 99)
number3 = random.randint(0, 99)

# Sum between of the three single-digit integers
print(f"The sum of between three single-digit integer, ({number1} + {number2} + {number3}) is "
      f"{number1 + number2 + number3}")
