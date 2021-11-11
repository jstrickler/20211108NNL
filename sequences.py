#!/usr/bin/python3

ctemps = [ -40, 0, 37, 75, 100 ]

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

# preferred -- list comprehension
clean_fruits = [f.strip().lower() for f in fruits]
print("clean_fruits (1):", clean_fruits, '\n')

# does not work
for f in fruits:
    clean_fruits = [f.strip().lower()]

print("clean_fruits (2):", clean_fruits, '\n')

# works but is too wordy
clean_fruits = []
for f in fruits:
    clean_fruits.append(f.strip().lower())
print("clean_fruits (3):", clean_fruits, '\n')