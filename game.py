import random
import time
# Needed for clear() function
from os import system, name
from time import sleep

# GLOBAL VARIABLES
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
# A dictionary is used to set values to each rank
values = {'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
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
        # This is a bit overcomplicated because you can never bet more than the total no. of chips you have
        # but I left it in for fun :)

        losses = self.total - self.bet

        # Ensure the total never goes below 0
        self.total = max(0, losses)

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
                print(f"You don't have enough chips to bet that much! You only have {chips.total}.")
            elif chips.bet < 0:
                print("You can't bet a negative amount of chips!")
            else:
                print(f"You bet {chips.bet} of your chips.")
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

    print("\nDEALER HAND:")
    # hide the first card and show the second card
    print("??????")
    print(dealer.cards[1])
    print(f"Point(s): ????")

    print("\nPLAYER HAND:")
    # show all the player's cards
    for card in player.cards:
        print(card)
    print(f"Point(s): {player.value}")

def show_all(player, dealer):
    """ Shows everyone's cards """

    print("\nDEALER HAND:")
    for card in dealer.cards:
        print(card)
    print(f"Point(s): {dealer.value}")

    print("\nPLAYER HAND:")
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

def clear():
    """
        Clears the terminal - works for Windows, Mac, and Linux
    """
    # For windows
    if name == 'nt':
        _ = system('cls')
    # For mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# The game begins here!
if __name__ == "__main__":

    # Set up the Player's chips
    # Can change the number of starting chips by putting a number in for the argument
    # Default is 100
    player_chips = Chips()

    # Keeps looping unless the player decides to stop playing again
    while True:
        # Welcome to Blackjack
        print("Welcome to Blackjack!")

        # Set up a new deck, the player and dealer's hand, and shuffle the deck
        game_deck = Deck()
        player_hand = Hand()
        dealer_hand = Hand()
        game_deck.shuffle()

        # Deal two cards to each person
        player_hand.add_card(game_deck.deal())
        player_hand.add_card(game_deck.deal())

        dealer_hand.add_card(game_deck.deal())
        dealer_hand.add_card(game_deck.deal())

        # Prompt the player to place a bet
        take_bet(player_chips)

        # Show one of the dealer's cards and the player's cards
        show_some(player_hand, dealer_hand)

        # Keep playing until the player stops hitting or busts
        while playing:
            # Prompt the player to hit or stay
            hit_or_stay(game_deck, player_hand)

            # Show one of the dealer's cards and the player's cards
            show_some(player_hand, dealer_hand)

            # If the player's hand exceed's 21, then they busted
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

        # If the player hasn't busted (decided to stay), then play the Dealer's hand until they reach 17 or greater
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                # Show all the dealer's cards and the player's card
                show_all(player_hand, dealer_hand)

                # Dealer keeps hitting...
                hit(game_deck, dealer_hand)
                print("Dealer hit...")
                time.sleep(1.5)

            clear()
            # Show everyone's final hand
            print("FINAL HANDS", end = "")
            show_all(player_hand, dealer_hand)

            # Check win conditions
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)
            elif player_hand.value > dealer_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            elif player_hand.value < dealer_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            elif player_hand.value == dealer_hand.value:
                push(player_hand, dealer_hand)

        # Show how many chips the player has
        print(f"\nYou have {player_chips.total} chips now!")

        # Ask the player if they want to play again
        play_again = input("Would you like to play again (y/n)? ")
        if play_again == 'y' or play_again == 'Y':

            # Check if the player has any chips left
            if player_chips <= 0:
                print("Sorry! You have no chips left.")
                break

            continue
        else:
            break
