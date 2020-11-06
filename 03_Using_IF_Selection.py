###############################
# Use IF Selection
###############################

# write boolean ekspression evaluates 'True'
print('\nExample 01 :')
# defined age
age = eval(input('Enter your age : '))

if 13 < age <= 18:
    print(True)
else:
    print(False)

print('\nExample 02 :')
# Defined your weight or height
weight, height = eval(input('Enter your weight and height : '))     # value separated by commas(,)

if weight > 50 or height > 160:
    print(True)
else:
    print(False)

print('\nExample 03 :')
# Defined your weight and height
weight, height = eval(input('Enter your weight and height : '))     # value separated by commas(,)

if weight > 50 and height > 160:
    print(True)
else:
    print(False)

print('\nExample 04 :')
# Defined your weight and height
# true if either weight is greater than 50 or
# height is greater than 160 , but not both

weight, height = eval(input('Enter your weight and height : '))     # value separated by commas(,)

if weight > 50 or height > 160:
    print(True)
if (weight > 50 or height > 160) and (weight > 50 and height > 160):
    if weight > 50 and height > 160:
        print('Not Both')

print('\nExample 05 :')
print("Define Leap Year")
# A leap year is a year if it is divisible by 4 but not by 100 or if it is divisible by 400
year = eval(input('Enter a year : '))

# Check if the year is a Leap year
isLeapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Display the result
print(f"Is a Leap year? {isLeapYear}")
