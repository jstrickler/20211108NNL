import sys
import os
# sys.path.append('DATA')  # search 'DATA' for modules and packages

states1 = ['CA', 'CO', 'CT', 'ND', 'NJ', 'VA', 'NC']
states2 = ['VA', 'FL', 'TX', 'ND', 'CA', 'OR', 'CO', 'ID', 'ME']

s1 = set(states1)
s2 = set(states2)
s1.add('CO')
s1.add('CO')
s1.add('SC')
print("s1:", s1)
print("s2:", s2, '\n')

print("common:", s1 & s2)  # intersection
print("not common:", s1 ^ s2)  # Xor (AKA symmetric difference)
print("all states:", s1 | s2)  # union
print("only s1:", s1 - s2)
print("only s2:", s2 - s1)

# os.chdir('DATA')
with open('DATA/breakfast.txt') as breakfast_in:
    unique_foods = set(line.rstrip() for line in breakfast_in)
print(unique_foods)

unique_foods.remove('spam')
print(unique_foods)
print(len(unique_foods))
