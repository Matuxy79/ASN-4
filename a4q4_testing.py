#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

#importing the object
from a4q4 import Card
import random

# Test for Card.create()
cards = Card.create()
if len(cards) == 52:
    print("Card.create() test passed.")
else:
    print("Card.create() test failed.")

# Test for Card.deal()
deck = Card.create()
cards_dealt = Card.deal(5, 3, deck)
if len(deck) == 52 - (5 * 3):
    print("Card.deal() test passed.")
else:
    print("Card.deal() test failed.")

# Test for Card.value()
card = "KD"
if Card.value(card) == 13:
    print("Card.value() test passed.")
else:
    print("Card.value() test failed.")

# Test for Card.highest()
cards = ["5D","10H","QS","8C","JH"]
if Card.highest(cards) == "QS":
    print("Card.highest() test passed.")
else:
    print("Card.highest() test failed.")

# Test for Card.lowest()
cards = ["5D","10H","QS","8C","JH"]
if Card.lowest(cards) == "5D":
    print("Card.lowest() test passed.")
else:
    print("Card.lowest() test failed.")

# Test for Card.average()
cards = ["5D","10H","QS","8C","JH"]
if Card.average(cards) == 8.2:
    print("Card.average() test passed.")
else:
    print("Card.average() test failed.")
