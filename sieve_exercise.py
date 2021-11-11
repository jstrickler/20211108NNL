
LIMIT = 1001
flags = [True] * LIMIT
for num in range(2, LIMIT):
    if flags[num]:  # is num prime?
        print(num, end=', ')
        for i in range(num * 2, LIMIT, num):
            flags[i] = False  # mark the non-primes
print('\n')
print(flags)