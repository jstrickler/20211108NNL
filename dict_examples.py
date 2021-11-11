d1 = dict()  #  empty dictionary
d2 = {}   # empty dict
d3 = dict(NC="Raleigh", NY="Albany")

state_caps =  {'NC': 'Raleigh', 'NY': 'Albany', 'SC': 'Columbia', 'PA': 'Harrisburg'}
state_caps['TX'] = 'Austin'
state_caps['CA'] = 'Sacramento'
print(state_caps)
state_caps['FL'] = 'Tallahassee'
print(state_caps)
print(len(state_caps))

print(state_caps['SC'])
print(state_caps['TX'])

for state in 'NC', 'TX', 'WA', 'NJ', 'CA':
    print(state, state in state_caps)
print()

print(state_caps.get('WA'))
print(state_caps.get('CA'))
print(state_caps.get('AR', 'not found'))

print(state_caps.setdefault('OR', 'Salem'))
print(state_caps)

state_caps['NC'] = 'Durham'

print(state_caps.keys())
print(state_caps.values(), '\n')

for state, capital in state_caps.items():
    print(state, capital)
print()

print(state_caps.items(), '\n')  # similar to enumerate(iterable)

del state_caps['OR']
print(state_caps)

colors = {'red': 0, 'blue': 0, 'purple': 0}
print(colors)
colors['red'] = colors['red'] + 1
colors['red'] += 1
colors['blue'] += 1
colors['blue'] += 1
print(colors)

data = ['red', 'red', 'purple', 'blue', 'purple', 'red', 'green', 'white']
for color in data:
    # if color not in colors:
    #     colors[color] = 0
    # colors[color] += 1
    colors[color] = colors.get(color, 0) + 1   # tricky??!
print(colors)










