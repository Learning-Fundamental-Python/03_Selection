# Write a simple program for solving Quadratic Equations for ax2 + bx + c = 0
import math

# Prompt user for input three numbers
a, b, c = eval(input('Enter three numbers : '))          # Separated by commas (,)

formula = (b * b) - (4 * a * c)
r1 = ((-b + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a))
r2 = ((-b - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a))

if formula > 0:
    print("The equation has two real roots")
    print(f"root 1 is {r1:.3f}")
    print(f"root 2 is {r2:.3f}")
elif formula == 0:
    print("The equation have one root")
    print(f"the root is {r1}")
else:
    print("The equation has no real roots")
