#!/usr/bin/env python

import random

fruit = ['apple', 'banana', 'cherry', 'date', 'elderberry',
    'fig', 'grapefruit', 'kiwi', 'orange', 'papaya', 'raspberry',
    'durian', 'grape', 'mango', 'lemon', 'pear', 'watermelon' ]

for i in range(1, 11):
    print("random():", random.random())
    print("randint(1, 2000):", random.randint(1, 2000))
    print("randrange(1, 5):", random.randrange(1, 5))
    print("choice(fruit):", random.choice(fruit))
    print("sample(fruit, 3):", random.sample(fruit, 3))
    print()
