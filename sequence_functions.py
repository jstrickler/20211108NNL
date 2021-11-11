
names = ['Fred', 'Daphne', 'Velma', 'Shaggy']
values = (5, 18, 3, 14, 76)
animal = "~Wombat 2/3"

objects = names, values, animal
for obj in objects:
    print(obj, len(obj), sorted(obj), min(obj), max(obj))
print()

print(sum(values))

print(names)
rnames = reversed(names)
print(rnames)
for name in rnames:
    print(name)
print()

capitals = ['Albany', 'Harrisburg', 'Durham', 'Columbia']
states = ['NY', 'PA', 'NC', 'SC']
animals = ['wolverine', 'ferret', 'red wolf', 'opossum']

state_caps = zip(capitals, states, animals)
print(state_caps)
for capital, state, animal in state_caps:
    print(capital, state)

state_caps = zip(capitals, states, animals)
print(list(state_caps))

for name in names[::-1]:   # makes a copy of names
    print(name)
print()




for name in reversed(names):  # does not make a copy of names
    print(name)
print()

# ugly and weird
for i in range(len(names)-1, -1, -1): # does not make a copy, but feweeeeeeeee
    print(names[i])

print('-' * 60)

i = 0
for name in names:
    print(i, name)
    i += 1
print()

for i, name in enumerate(names):
    print(i, name)
print(list(enumerate(names)), '\n')

x = ['a', 'b', 'c']
y = ['d', 'e', 'f']
print(x + y)
print("foo" + "bar")
print(x * 3)
print(y * 2)
flags = [True] * 10
print(flags)
print('-' * 60)
print("wombat " * 8)


