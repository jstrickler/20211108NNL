list1 = list()  # empty list
list2 = ['a', 'b', 'c', 1, 2, 3, None, 5.8]
list3 = []  # empty list

cities = ['Albany', 'Schenectady', 'Pittsburgh', 'Homestead',
          'McKeesport', 'Charleston']
print(cities[0], cities[5], cities[len(cities)-1], cities[-1])
print(cities)
print(" ".join(cities))
print(" & ".join(cities))
cities.insert(0, 'Durham')
cities.insert(3, 'Troy')
print(cities)
cities.append('Monroeville')
cities.append("Lexington")
print(cities)
more_cities = ['Sewickley', 'Clemson']
cities.extend(more_cities)
print(cities)
cities.append("Colonie")
cities.insert(2, 'East Greenbush')
print(cities)
# LIST.insert(pos, obj)  LIST.append(obj)  LIST.extend(iterable)
del cities[2]
print(cities)

c = cities.pop()
print(c)
print(cities)

c = cities.pop(3)
print(c)
print(cities)

cities.remove('McKeesport')
print(cities)

# INVALID
# cities.remove()
# cities.remove("Raleigh")

#  del LIST[pos]   LIST.pop(pos=-1)   LIST.remove(value)

print(cities.index('Pittsburgh'))
# print(cities.index('Raleigh'))
print("Pittsburgh" in cities)
print("Raleigh" in cities)

print(cities)
print(cities[0:4])   # 0..3    OR  0 + 4 items
#  LIST[START:STOP]   LIST[:STOP]  LIST[START:]  LIST[:]
print(cities[3:6])

actor = "Chris Hemsworth"
print(actor[:3], actor[-5:].upper(), actor[6:9])

print(cities)
cities[1] = 'Troy'
print(cities)

cities.insert(0, cities.pop(1))
print(cities)

cities[:3] = reversed(cities[:3])
print(cities)

cities.reverse()   # cities = list(reversed(cities))
cities.insert(8, 'Pittsburgh')
cities.insert(0, 'Pittsburgh')
cities.append('Pittsburgh')
print(cities)
# pos = -1
# old_pos = None
# while pos < len(cities):
#     old_pos = cities.index('Pittsburgh', pos + 1)
#     if pos == old_pos:
#         break
#     else:
#         pos = old_pos
#     print(pos)
# print()
#
# print(cities)
print()
for city in cities:
    # city = cities[0]
    # city = cities[1]
    # ...
    print(city)
print()

# for VAR in ITERABLE:
#   ....

s = "abc"
for char in s:
    print(char)
print()

for city in cities[:4]:
    print(city)
print()

item = 'a'
# ...
item = 5
item = None
# ...

junk = ['a', 5, None, 37.2]
for item in junk:
    print(item, type(item))
print()

# not recommended
# for i in range(len(cities)):
#     print(cities[i])
# print()

for city in cities:
    print(city)

print(cities)
print(cities[::2], '\n')
print(cities[1::2], '\n')

for city in cities[::2]:
    print(city)  # every other city
print()