#!/usr/bin/env python
#    module           class
from carddeck import CardDeck
from joker_deck import JokerDeck
#creates an instance of the class

d1 = CardDeck("Scotty")
print(d1)
#
# d1.shuffle()
# for i in range(5):
#     print(d1.draw())

d2 = CardDeck('Jess')
print(d2)
print(d2.dealer)

d2.dealer = 'Kara'
print(d2.dealer)



d1.shuffle()
print(d1.cards)


hand = []

for i in range(5):
    hand.append(d1.deal())

print(hand, '\n')

print(len(d1), "cards left")
print(d1)

b = d1 + d2
print(b)
b.shuffle()
print(b.deal())

print("-"*60)
j1 = JokerDeck('Laura')
j1.shuffle()
print(j1.deal())
print(len(j1))