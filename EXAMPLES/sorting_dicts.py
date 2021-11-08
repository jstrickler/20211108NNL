#!/usr/bin/python3

count_of = dict(red=5, green=18, blue=1, pink=0, grey=27, yellow=5)

# sort by key
for color, num in sorted(count_of.items()):
    print(color,num)

print()

# sort by value
for color, num in sorted(count_of.items(), key=lambda e: e[1]):
    print(color,num)


