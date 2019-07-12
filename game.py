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
        """ Cards are created with a suit and rank """

        self.suit = suit
        self.rank = rank

    def __str__(self):
        """ Prints the rank and suit of the card """

        return f"{self.rank} of {self.suit}"

class Deck:
    """ Deck class to keep track of the cards and to be shuffled """

    global suits, ranks

    def __init__(self):
        """ Default deck has 52  (13 ranks per suit) """

        # Initiate the empty deck
        self.deck = []

        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        """ Shuffles the deck """

        random.shuffle(self.deck)

    def deal(self):
        """ Removes the top 4 cards of the deck """

        dealt_cards = []

        for i in range(0, 4):
            dealt_cards.append(self.deck.pop())

        return dealt_cards

class Hand:
    """ Hand class to hold Card objects from the Deck class. """

    global values

    def __init__(self):
        """ Starting Hand has no cards, so Hand has no value """

        # start with an empty hand
        self.cards = []
        # keep track of value of hand
        self.value = 0
        # keep track of aces
        self.aces = 0

    def add_card(self, card):
        """ Add a card to Hand """

        # Add the card to the player's hand list
        self.cards.append(card)
        # Store the value of the card
        self.value += values[card.rank]

    def adjust_for_ace(self):
        pass

class Chips:
    """ Keeps track of the Player's starting chips, bets, and ongoing wins """

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        pass

    def lose_bet(self):
        pass

def take_bet():
    """ Asks the user for an integer value to bet. Will keep asking until an integer is inputted """

    while True:
        try:
            ans = int(input("How much do you want to bet this round: "))
        except ValueError:
            print("That isn't a number. Try again.")
            continue
        else:
            print("Thank you for placing your bet")
            break

my_deck = Deck()
my_deck.shuffle()
dealer = my_deck.deal()
#print(dealer[0].rank)
for card in dealer:
    print(card)

my_hand = Hand()
my_hand.add_card(dealer[0])
print(my_hand.value)

take_bet()
