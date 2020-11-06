##########################################
# Use Logical operator in Selection
##########################################
# The logical operators not , and , and or can be used to
# create a composite condition

print('Example 01 :')
# Use logical operator in selections
# Receive an input

number = eval(input('Enter an integer : '))

if number % 2 == 0 and number % 3 == 0:
    print(f"{number} is divisible by 2 and 3")
if number % 2 == 0 or number % 3 == 0:
    print(f"{number} is divisible by 2 or 3")
if (number % 2 == 0 or number % 3 == 0) and \
        not (number % 2 == 0 and number % 3 == 0):
    print(f"{number} is divisible by 2 or 3, but not both")

print('\nExample 2 :')
x = 1
print(True and (3 > 4))
print(not (x > 0) and (x > 0))
print((x > 0) or (x < 0))
print((x != 0) or (x == 0))
print((x >= 0) == (not (x == 1)))

print('\nExample 3 :')
# Write a boolen ekspression use AND operator
number = eval(input('Enter number between 1 and 100 : '))

if 0 < number <= 100:
    print(True)
else:
    print('Input Wrong!...')
    print('Input number between 1 and 100')

print('\nExample 4 :')
# Write a boolen ekspression use OR operator
number = eval(input('Enter number between 1 and 100 or negative number : '))

if number < 1 or (1 <= number <= 100):
    print(True)
else:
    print('Input Wrong!...')
    print('Input number between 1 and 100')

print('\nExample 5 :')
# write boolean ekspression using 3 numbers
x, y, z = eval(input('Enter three number : '))

print(f"(x < y and y < z) is {x < y < z}")
print(f"(x < y or y < z) is {x < y or y < z}")
print(f"not(x < y) is {not (x < y)}")
print(f"(x < y < z) is {x < y < z}")
print(f"not(x < y < z) is {not (x < y < z)}")
