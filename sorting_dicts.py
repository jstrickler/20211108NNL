airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print(airports.items())

for code, name in sorted(airports.items()):
    print(code, name)
print("-" * 10)

def by_value(kv_pair):
    return kv_pair[1], kv_pair[0]

for code, name in sorted(airports.items(), key=by_value):
    print(code, name)
print("-" * 10)