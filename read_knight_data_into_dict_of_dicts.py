from pprint import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        name, title, color, quest, comment = raw_line.rstrip().split(':')
        knight_data[name] = {
            'title': title,
            'color': color,
            'quest': quest,
            'comment': comment,
        }

pprint(knight_data, sort_dicts=False)   # 3.8 and later
print(knight_data['Arthur']['title'])

for name, data in knight_data.items():
    print(data['title'], name)
print()