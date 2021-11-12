
nums = [800,80,1000,32,255,400, 5,5000]
n1 = sorted(nums)
print("n1:", n1, '\n')
n2 = sorted(nums, reverse=True)
print("n2:", n2, '\n')

fruits = ["pomegranate", "cherry", "apricot", "Apple",
" lemon", " Kiwi", "ORANGE ", "lime", "Watermelon", "guava",
"Papaya", "FIG", " pear", "banana", "  Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "Banana", "lychee", "GRAPE", "date"]

f1 = sorted(fruits)
print("f1:", f1, '\n')

def ignore_case(f):
    lower_f = f.lower()
    print(f"comparing {f} as {lower_f}")
    return lower_f


f2 = sorted(fruits, key=ignore_case)   # "key" means "key_function"
print("f2:", f2, '\n')
x = "abc"
x.lower()

f3 = sorted(fruits, key=str.lower)
print("f3:", f3, '\n')

f4 = sorted(fruits, key=len)
print("f4:", f4, '\n')

def mysort(f):
    return len(f.strip()), f.strip().lower()

f5 = sorted(fruits, key=mysort)
print("f5:", f5, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15', [1, 3, 9]),
    ('Steve', 'Jobs', 'Apple', '1955-02-24', [8, 4, 3]),
    ('Larry', 'Wall', 'Perl', '1954-09-27', [9, 6, 2]),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21', [1, 3, 9]),
    # ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    # ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    # ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    # ('Sergey','Brin', 'Google', '1973-08-21'),
    # ('Larry', 'Page', 'Google', '1973-03-26'),
    # ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people):
    print(person)
print("-" * 60)

def by_last_name(person):
    return person[1], person[0]

for person in sorted(people, key=by_last_name):
    print(person)
print("-" * 60)

def by_dob(p):
    return p[-1]

for first_name, last_name, product, dob, junk in sorted(people, key=by_dob):
    print(first_name, last_name, dob)
print("-" * 60)

for first_name, last_name, product, dob, junk in sorted(people, key=lambda p: (p[4][0], p[3])):
    print(last_name, dob, junk)
print("=" * 60)

print(nums)
print(sorted(nums))
print(nums)
nums.sort()
print(nums)


