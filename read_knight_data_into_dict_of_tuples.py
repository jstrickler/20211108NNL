from pprint import pprint

def main():
    d = get_data()
    pretty_print(d)
    print()
    print(get_item(d, 'Arthur', 2))
    print(get_item(d, 'Lancelot', 0))
    print()
    display_names_titles(d)

def get_data():
    knight_data = {}
    with open('DATA/knights.txt') as knights_in:
        for raw_line in knights_in:
            name, title, color, quest, comment = raw_line.rstrip().split(':')
            knight_data[name] = title, color, quest, comment
    return knight_data

def pretty_print(data):
    pprint(data, sort_dicts=False)   # 3.8 and later

def get_item(data, knight, item_index):
    if item_index < 0 or item_index > 3:
        raise IndexError("Only values 0-3 are allowed as indexes")
    return data[knight][item_index]

def display_names_titles(data):
    for name, fields in data.items():
        print(fields[0], name)
    print()

main()
