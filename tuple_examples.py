person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'  # tuple

ta = 5,  # one-element tuple
tb = ()  # zero-element (empty) tuple

print(person)
print(len(person), person[0], person[-1], person[:2])

# var1, var2, ... = iterable

first_name, last_name, product, dob = person
print(first_name, last_name)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
]
print(people[0])
print(people[0][0])
print(people[0][0][0])
print()

for first_name, last_name, *product, dob in people:
    # first_name, last_name, product, dob = people[0]
    # first_name, last_name, product, dob = people[1]
    # ...
    print(first_name, last_name, product)

values = ['a', 'b', 'c', 'd', 'e', 'f']
x, y, *z = values
print(x, y, z)
x, *y, z = values
print(x, y, z)
*x, y, z = values
print(x, y, z)
print()

clients = [('Fred', 24), ('Velma', 22), ('Daphne', 21), ('Shaggy', 25)]
for name, age in clients:
    print(f"{name} is {age} years old")
print()

client_names = []
for name, age in clients:
    client_names.append(name)
print("client_names:", client_names)
client_names = [c[0] for c in clients]  # list comprehension
print("client_names:", client_names)




