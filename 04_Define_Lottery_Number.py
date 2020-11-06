"""
The lottery program in this case study involves generating random numbers,
comparing digits, and using Boolean operators
"""
import random

# Generate a lottery number
lottery = random.randint(0, 99)

# Prompt the user to enter a guess
guess = eval(input("Enter your lottery pick (two digits) : "))

# Get digits from lottery
lottery_Digit1 = lottery // 10
lottery_Digit2 = lottery % 10

# Get digits from guess
guess_digit1 = guess // 10
guess_digit2 = guess % 10

print(f"The lottery number is {lottery}")

# Check the guess
if guess == lottery:
    print("Exact match : you win $10,000")
elif (guess_digit1 == lottery_Digit1 and
      guess_digit2 == lottery_Digit2):
    print("Match all digits: you win $3,000")
elif (guess_digit1 == lottery_Digit1
      or guess_digit1 == lottery_Digit2
      or guess_digit2 == lottery_Digit1
      or guess_digit2 == lottery_Digit2):
    print("Match one digit: you win $1,000")
else:
    print("Sorry, No match...")
