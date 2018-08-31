#!/usr/bin/env python
import random

class CardDeck():
    RANKS  = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = 'Clubs Diamonds Hearts Spades'.split()

# constuctor (always called when the class is ubsttainited
    def __init__(self, dealer):
        self._dealer = dealer
        self._create_deck()

    def _create_deck(self):
        self._cards = []
        for s in self.SUITS:
            for r in self.RANKS:
                self._cards.append((r,s))

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self):
        return self._cards.pop()

    @property #getter
    def dealer(self):
        return self._dealer

    @dealer.setter # setter
    def dealer(self,dealer):
        if isinstance(dealer,str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    @property
    def cards(self):
        return self._cards

    def __len__(self):
        return len(self._cards)

    def __str__(self):
        my_type = type(self)
        my_name = my_type.__name__
        return f"{my_name}({len(self)})"

    def __add__(self,other):
        tmp = type(self)(self.dealer)
        tmp._cards = self.cards + other.cards
        return tmp


