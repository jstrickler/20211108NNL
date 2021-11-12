import sqlite3

file_path = "DATA/wombats.txt"
try:
    with open(file_path) as file_in:
        pass
except (FileNotFoundError, PermissionError) as err:
    print(err)

numbers = [5, 8, 0, 15, 42, 3, 1]
try:
    print(numbers[12])
except IndexError as err:
    print(err)

value = 23
for n in numbers:
    try:
        result = value / n
    except ZeroDivisionError as err:
        print(err)
    except Exception as err:  # generic error -- catches any other error
        print(err)
    else:  # no exception
        print(result)

conn = None
try:
    with sqlite3.connect('DB/fishes.db') as conn:
        cursor = conn.cursor()
        cursor.execute('select * from fish')
        for row in cursor.fetchall():
            print(row)
except sqlite3.OperationalError as err:
    print(err)
finally:  # guaranteed to exit whether exception or not
    if conn is not None:
        conn.close()
print("All done.")