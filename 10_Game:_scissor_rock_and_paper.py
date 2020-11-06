"""
Write a program that plays the popular scissor-rock-
paper game. (A scissor can cut a paper, a rock can knock a scissor, and a paper can
wrap a rock.) The program randomly generates a number 0 , 1 , or 2 representing
scissor, rock, and paper. The program prompts the user to enter a number 0 , 1 , or
2 and displays a message indicating whether the user or the computer wins, loses,
or draws.
"""
import random

# 0 = scissor, 1 = rock, 2 = paper
computer = random.randint(0, 2)

# Prompt user to input 0 - 2 (scissor, rock or paper)
user = eval(input("Enter an integer between 0 and 2 : "))

if (user == 0 and computer == 0) or (user == 1 and computer == 1) \
        or (user == 2 and computer == 2):
    print("It's a draw")
    print(f"The computer is {computer} and You are {user}")
elif user == 0 and computer == 1:
    print("You Lose")
    print(f"The computer is {computer} and You are {user}")
elif user == 0 and computer == 2:
    print("You won")
    print(f"The computer is {computer} and You are {user}")
elif user == 1 and computer == 0:
    print("You won")
    print(f"The computer is {computer} and You are {user}")
elif user == 1 and computer == 2:
    print("You Lose")
    print(f"The computer is {computer} and You are {user}")
elif user == 2 and computer == 0:
    print("You Lose")
    print(f"The computer is {computer} and You are {user}")
elif user == 2 and computer == 1:
    print("You won")
    print(f"The computer is {computer} and You are {user}")
else:
    print("Your Input Error")
    print("Input an integer between 0 and 2")
