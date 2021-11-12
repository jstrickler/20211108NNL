import sqlite3

file_path = "DATA/wombats.txt"
with open(file_path) as file_in:
    pass

numbers = [5, 8, 0, 15, 42, 3, 1]
print(numbers[12])

value = 23
for n in numbers:
    result = value / n
    print(result)

with sqlite3.connect('DB/fishes.db') as conn:
    cursor = conn.cursor()
    cursor.execute('select * from fish')
