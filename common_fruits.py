with open('DATA/fruit1.txt') as fruit1_in:
    fruits1 = [line.rstrip().lower() for line in fruit1_in]

with open('DATA/fruit2.txt') as fruit2_in:
    fruits2 = [line.rstrip().lower() for line in fruit2_in]

print(fruits1)
print(fruits2)

f1 = set(fruits1)
f2 = set(fruits2)
print()
print(f1)
print(f2)
print(f1 & f2)
print(f1 ^ f2)
