#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16


import random
#The Card class has a list of suits and a dictionary of values, where each card is represented as a string with its value and suit concatenated together.
class Card:
    suits = ['H', 'D', 'S', 'C']
    values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}

    def create():
        """
        The method generates and returns a full deck of cards as a list
        """
        deck = []
        for suit in Card.suits:
            for value in Card.values:
                deck.append(value + suit)
        return deck


    def deal(num_cards, num_players, deck):
        """
        The method takes in the number of cards to be dealt, the players and the deck. Then it shuffles said deck and deals the cards to the players removing them from the overall deck and putting them into hands
        Each hand is a list of cards from the deck
        """
        random.shuffle(deck)
        hands = []
        for i in range(num_players):
            hand = []
            for j in range(num_cards):
                if len(deck) > 0:
                    card = deck.pop()
                    hand.append(card)
            hands.append(hand)
        return hands

    def value(card):
        """
        This method looks up and returns the value of the card from the dictionary
        """
        return Card.values[card[:-1]]

    def highest(list_of_cards):
        """
        This method takes in the list of cards and returns the highest value card
        """
        return max(list_of_cards, key=Card.value)

    def lowest(list_of_cards):
        """
        This method takes in the list of cards and returns the highest value card
        """
        return min(list_of_cards, key=Card.value)

    def average(list_of_cards):
        """
        It takes in a list of cards and returns the average value by summing up the values of each card and dividing by the number of cards. If the list is empty, it returns 0.
        """
        total = sum(Card.value(card) for card in list_of_cards)
        return total / len(list_of_cards) if len(list_of_cards) > 0 else 0
