#!/usr/bin/python3

import random

fruits = ['apple','banana','cherry','date','elderberry',
    'fig','grapefruit','kiwi','orange','papaya','raspberry', 
    'durian','grape','mango','lemon','pear','watermelon' ]

for i in range(1,11):
    print("random():",random.random())
    print("randint(1,2000):",random.randint(1,2000))
    print("randrange(1,5):",random.randrange(1,5))
    print("choice(fruits):",random.choice(fruits))
    print("sample(fruits,3):",random.sample(fruits,3))
    print()

