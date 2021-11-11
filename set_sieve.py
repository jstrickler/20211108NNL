
limit = 1000000

non_prime = set()

for num in range(2, limit+1):
    if num not in non_prime:
        print(num, end=' ')
        for m in range(num * 2, limit + 1, num):
            non_prime.add(m)
