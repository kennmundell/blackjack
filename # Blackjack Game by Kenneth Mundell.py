# Blackjack Game by Kenneth Mundell

import random
print("Welcome to black jack")
#cards = {}
#play_cards()

#while game is True:


cards = ["2","3","4","5","6","7","8","9","10", "Jack", "Queen", "King", "Ace"]

hand = random.choices(cards, k=2)

computer_hand = random.choices(cards, k=2)
print("Your hand is " + str(hand))
print("Computer hand is " + str(computer_hand))
print()

choice = input("Do you want another card or do you want to stick?")