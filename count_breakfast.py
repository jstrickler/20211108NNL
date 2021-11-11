from collections import Counter

counts = {}
with open('DATA/breakfast.txt') as breakfast_in:
    for raw_line in breakfast_in:
        food = raw_line.rstrip()
        if food not in counts:
            counts[food] = 0
        counts[food] += 1

print(counts)

print(type(breakfast_in))

with open('DATA/breakfast.txt') as breakfast_in:
    c = Counter(food.rstrip() for food in breakfast_in)
    c['Eggs Benedict'] += 1
    c['raisin bran'] += 1
print(c)
print(c.items())
print(c.keys())
del c['raisin bran']
print(c)

