i = 0
while i < 3:
    print(i)
    i += 1
print()

while True:
    user_name = input("Enter name (or q to quit): ")
    if user_name == 'q':
        break  # exit loop
    if user_name == '':
        continue  # go to top

    print(f"Hello, {user_name}")

