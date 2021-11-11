import math

def circle_area(diameter):
    radius = diameter / 2
    area = math.pi * radius ** 2
    return area

a = circle_area(10)
print(a)
print(circle_area(18.6))

def bark():
    print("Woof! woof!")
    # return None

x = bark()
print("bark returns:", x)

# def do_circles():
#     while True:
#         raw_diameter = input("Enter diameter of circle (or q to quit): ")
#         if raw_diameter == 'q':
#             break
#         diameter = float(raw_diameter)
#         area = circle_area(diameter)
#         print(f"The area of a circle with diameter {diameter} is {area}")

# do_circles()

def first_last(a_list):
    return a_list[0], a_list[-1]  # one object

items = ['a', 'b', 'c', 'd', 'e']

result = first_last(items)
print(result)

# no-star, star, no-star, double-star
def wacky(p1, p2, *p3, p4, p5, **p6):
    pass

def rectangle_area(length, width):
    return length * width

print(rectangle_area(10, 18))

def find_letter(letter, *file_paths, ignore_case=False):
    print("file_paths:", file_paths)
    found_lines = []
    if ignore_case:
        letter = letter.lower()
    for file_path in file_paths:
        with open(file_path) as file_in:
            for raw_line in file_in:
                original_line = raw_line
                if ignore_case:
                    raw_line = raw_line.lower()
                if letter in raw_line:
                    line = raw_line.rstrip()
                    found_lines.append((file_path, original_line.rstrip()))
    return found_lines

files_to_search = 'DATA/presidents.txt', 'DATA/parrot.txt'

results = find_letter('z', *files_to_search)
print(results)
print()

results = find_letter('lizard', 'DATA/alice.txt', ignore_case=True)
print(results, '\n')

def config(**values):
    print("values:", values)

config(file_name="wombats.txt", animal="wombat", ignore_case=False)

import lxml.etree as et

xml_tag = et.Element('span', id="foo", spam="ham")
print(et.tostring(xml_tag).decode())

def Element(tag, **attrs):
    pass

