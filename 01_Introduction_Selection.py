##########################################
# Introduction Selections
# Make a program can decide which statements
# to execute based on a condition
##########################################
import math
import random

print('Example 01 :')
# Compute area of circle based on value of radius
radius = eval(input('Enter radius of Circle : '))

# Using selections
if radius < 0:
    print('Incorret input')
else:
    area = math.pi * radius * radius
    print(f"The area of circle with radius {radius} is {area:.2f} m2")

print('Using boolean ekspression in statement')
# A Boolean expression is an expression that evaluates
# to a Boolean value True or False

print('\nExample 02 :')
i = int(True)
j = int(False)

b1 = bool(4)
b2 = bool(0)

print(i)
print(j)
print(b1)
print(b2)

print('\nExample 03 :')
print('Generating Random Numbers')

# Generate random numbers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# Prompt the user to enter an answer
answer = eval(input("What is " + str(number1) + " + " + str(number2) + " ? "))

# Display the result
print(f"{number1} + {number2} = {answer}  is {number1 + number2 == answer}")

print('\nSingle IF Statement')
# A one-way if statement executes the statements if the condition is true

print('Example 04 :')
number = eval(input('Enter an integer : '))

if number % 5 == 0:
    print('HiFive')
if number % 2 == 0:
    print('HiEven')

print('\nExample 05 : ')
print('Two-Way IF-ELSE Statement')
# A two-way if-else statement decides which statements
# to execute based on whether the condition is true or false

# Compute of area based on input data radius
radius = eval(input('Enter value for radius circle : '))

if radius >= 0:
    area = math.pi * radius * radius
    print(f"The area for the circle of radius {radius} is {area:.2f} ")
else:
    print('Negative input')

print('\nExample 06 :')
# Defined a input number is even or odd
number = eval(input('Enter an integer : '))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

print('\nExample 07 :')
# Substraction between two numbers
# Defined the result True or False

# Generate two random single-digit integers
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# if number1 < number2, swap number1 with number 2
if number1 < number2:
    number1, number2 = number2, number1         # Simultaneous assignment

# Prompt the student to answer "What is number1 - number2 ?"
answer = eval(input("What is " + str(number1) + " - " + str(number2) + "? "))

# Check the answer and display the result
if number1 - number2 == answer:
    print('You are correct!...')
else:
    print(f"You answer is wrong.\n {number1} - {number2} is {number1 - number2}")


print('\nExample 08 :')
print('Nested IF and multiways IF-ELIF-ELSE Statements')
# Define the grade based on your score
score = eval(input('Enter your Score : '))

if score >= 90.0:
    grade = 'A'
elif score >= 80.0:
    grade = 'B'
elif score >= 70.0:
    grade = 'C'
elif score >= 60.0:
    grade = 'D'
else:
    grade = 'F'

print("Your Grade is", grade)

print('\nExample 09 :')
# Define chinese zodiac based on born of year
year = eval(input('Enter a year : '))
zodiac_year = year % 12

if zodiac_year == 0:
    print('Monkey')
elif zodiac_year == 1:
    print('Rooster')
elif zodiac_year == 2:
    print("Dog")
elif zodiac_year == 3:
    print("Pig")
elif zodiac_year == 4:
    print("Rat")
elif zodiac_year == 5:
    print("Ox")
elif zodiac_year == 6:
    print("Tiger")
elif zodiac_year == 7:
    print("Rabbit")
elif zodiac_year == 8:
    print("Dragon")
elif zodiac_year == 9:
    print("Snake")
elif zodiac_year == 10:
    print("Horse")
else:
    print("Sheep")

print("\nExample 10 :")
x = eval(input('Enter an integer : '))
y = eval(input('Enter an integer : '))

if x > 2:
    if y > 2:
        z = x + y
        print("z is", z)
    else:
        print("x is", x)

print("\nExample 11 :")
if x > 2:
    if y > 2:
        z = x + y
        print("z is", z)
else:
    print("x is", x)

print('\nExample 12 :')
print('Compute BMI')
# Body mass index (BMI) is a measure of health based on weight

# Prompt user to enter weight in pounds
weight = eval(input("Enter weight in pounds : "))

# Prompt user to enter height in inches
height = eval(input("Enter height in inches : "))

KILOGRAMS_PER_POUND = 0.45359237        # make a constant
METER_PER_INCH = 0.0254                 # make a constant

# Compute bmi
weight_inKilograms = weight * KILOGRAMS_PER_POUND
height_inMeters = height * METER_PER_INCH
bmi = weight_inKilograms / (height_inMeters * height_inMeters)

# Display result
print("BMI is", format(bmi, ".2f"))
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
