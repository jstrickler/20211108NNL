#!/usr/bin/python3

import sys

if len(sys.argv) > 1:
    raw_max = sys.argv[1]
else:
    raw_max = input("Enter maximum: ")

max = int(raw_max) + 1
min = 0
tries = 0

while True:
    guess = (max + min)//2
    ans = input("Is {0} your number? ".format(guess))

    if ans == "q":
        break

    tries = tries + 1

    if ans == "h":
        max = guess
    elif ans == "l":
        min = guess
    elif ans == "y":
        print("I got it in {0} try(ies)!".format(tries))
        break
    else:
        print("Please enter h, l, or y")
    

