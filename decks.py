"""Python library modeling card decks"""
# Work through this file by copying-and-pasting code from it into the python console
from collections import namedtuple

# We've used tuples as a way to bundle pieces of data together.
# If you just want an immutable bundle of values, but you want
# to be able to name the pieces of data within it instead of
# having to remember indices, *namedtuple* allows us to create
# a very basic class.

# A *class* is like a blueprint for creating objects.

Card = namedtuple('Card', ['rank', 'suit'])
# namedtuple returns a "class object" or "constructor"
# 1st parameter: name of the class
# 2nd parameter: list of names for the data members

# When you create an *instance* of Card, you can get rank and suit via dot notation
# ace = Card('A', 'spades')
# ace.rank  -> 'A'
# ace.suit  -> 'spades'

class FrenchDeck:  # class definition compound statement
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()


    # this function is run whenever you initialize a new object via FrenchDeck()
    def __init__(self):
        # the first parameter references the object we are working with
        # the convention is to use the name `self` for this reference
        # this parameter is automatically filled in when you use dot notation
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

# Python has a standard interface for how to interact with objects using these
# special functions called "dunder methods". Copy this class over into your console
# and try using some of the statements and functions we've learned in this course:
# for, reversed(), slices, random.choice()

# If we want to sort, we should probably make a "key" function
spades_high_values = {'spades': 3, 'hearts': 2, 'diamonds': 1, 'clubs': 0}

def spades_high(card: Card) -> int:
    rank_value = 0  # change to position of card.rank in FrenchDeck.ranks
    suit_value = 0  # change to value associated with card.suit in spades_high_values
    return rank_value * len(spades_high_values) + suit_value

# Now you can use sorted() to get a sorted order of the cards

# What about shuffling the deck? Try using random.shuffle() on a deck and see what happens.

# Write a function for setting the card at a position in the deck.
# Check to make sure that the card is actually a Card and raise
#     an appropriate exception if it is not.
def set_card(deck: FrenchDeck, position: int, card: Card) -> None:
    return

# You can "monkey patch" FrenchDeck in your console by typing:
# FrenchDeck.__setitem__ = set_card

# Now test and see if you can shuffle the deck!
