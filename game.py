import random

# GLOBAL VARIABLES
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
# A dictionary is used to set values to each rank
values = {'Ace': [1, 11], 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

# Boolean value to keep track of while loops
playing = True

class Card:
    """ Card class to keep track of suit and rank """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    """ Deck class to keep track of the cards and to be shuffled """

    global suits, ranks

    def __init__(self):
        # Initiate the empty deck
        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        pass

my_deck = Deck()
