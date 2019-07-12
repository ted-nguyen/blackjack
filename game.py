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
        """ Removes the card at the top of the deck """

        return self.deck.pop()

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

        # Check for aces
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):

        # If total value is greater than 21 and there is 1 or more aces still
        # Then change the value of the ace from 11 to 1
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1


class Chips:
    """ Keeps track of the Player's starting chips, bets, and ongoing wins """

    def __init__(self, total = 100):
        # This value can be changed; player starts with 100 chips
        self.total = total
        # How much is being bet
        self.bet = 0

    def win_bet(self):
        """ Adds the bet amount to their winnings """
        self.total += self.bet

    def lose_bet(self):
        """ Takes the bet amount from their winnings """
        self.total -= self.bet

def take_bet(chips):
    """ Asks the user for an integer value to bet. Will keep asking until an integer is inputted """

    while True:
        try:
            chips.bet = int(input("How much do you want to bet: "))
        except ValueError:
            print("That isn't a number. Try again.")
            continue
        else:
            if chips.bet > chips.total:
                print(f"You don't have enough chips to bet that much! You only have {chips.total}")
            else:
                print(f"You bet ${chips.bet}")
                break

def hit(deck, hand):
    """ Deals a card to the Hand """

    # Deal a card and add it to their hand
    one_card = deck.deal()
    hand.add_card(one_card)

    # Readjust the hand's value if their hand exceeds 21 and they have an ace
    hand.adjust_for_ace()

def hit_or_stay(deck, hand):
    """ If they Player decides to hit, calls the hit() function; otherwise playing is set to False """

    global playing

    while True:
        ans = input("Would you like to hit or stay?(h/s) ")

        if ans.lower() == 'h' or ans.lower() == 'hit':
            print("You decided to hit!\n")
            hit(deck, hand)
            playing = True
        elif ans.lower() == 's' or ans.lower() == 'stay':
            print("You decided to stay! Feeling lucky?\n")
            playing = False
        else:
            print("Please hit (h) or stay (s).")
            continue

        break

def show_some(player, dealer):
    """ Only shows the dealer's second card and the Player's card """

    print("Dealer's Hand:")
    # show the second card
    print(dealer.cards[1])
    print(f"Point(s): {dealer.value}")

    print("Player's Hand:")
    # show all the player's cards
    for card in player.cards:
        print(card)
    print(f"Point(s)): {player.value}")

def show_all(player, dealer):
    """ Shows everyone's cards """

    print("Dealer's Hand:")
    for card in dealer.cards:
        print(card)
    print(f"Point(s): {dealer.value}")

    print("\nPlayer's Hand:")
    for card in player.cards:
        print(card)
    print(f"Point(s): {player.value}")

def player_busts(player, dealer, chips):
    print("Player BUSTED! Better luck next time!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player WON!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer BUSTED! Player won their bet!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer WON! Player lost their bet.")
    chips.lose_bet()

def push(player, dealer):
    """ Prints a statement that the game was a tie """

    print("Player and Dealer tied! What are the odds?!")

game_deck = Deck()
player_hand = Hand()
dealer_hand = Hand()
game_deck.shuffle()


#the_chips = Chips()
#take_bet(the_chips)

hit_or_stay(game_deck, player_hand)
show_all(player_hand, dealer_hand)
