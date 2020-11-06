"""
Write a program that lets the user guess whether a flipped
coin displays the head or the tail. The program randomly generates an integer 0 or
1 , which represents head or tail. The program prompts the user to enter a guess
and reports whether the guess is correct or incorrect.
"""
import random
coin = random.randint(0, 1)

# prompts the user to enter a guess coin
guess = int(input('Enter your guess : '))

if coin == guess:
    print('Your Guess match')
    if guess == 1:
        print('Head')
    else:
        print('Tail')
else:
    print("Your guess doesn't match")
