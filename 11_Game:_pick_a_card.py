"""
Write a program that simulates picking a card from a deck of 52 cards.
Your program should display the rank ( Ace , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ,
Jack , Queen , King ) and suit ( Clubs , Diamonds , Hearts , Spades ) of the card.
"""
import random

card = random.randint(0, 12)
suit = random.randint(0, 3)

# Define your card
if card == 0:
    card = 'Ace'
elif card == 1:
    card = 2
elif card == 2:
    card = 3
elif card == 3:
    card = 4
elif card == 4:
    card = 5
elif card == 5:
    card = 6
elif card == 6:
    card = 7
elif card == 7:
    card = 8
elif card == 8:
    card = 9
elif card == 9:
    card = 10
elif card == 10:
    card = 'Jack'
elif card == 11:
    card = 'Queen'
else:
    card = 'King'

# Define your suit
if suit == 0:
    suit = 'Clubs'
elif suit == 1:
    suit = 'Diamonds'
elif suit == 2:
    suit = 'Hearts'
else:
    suit = 'Spades'

print(f"The card you picked is the {card} of {suit}")