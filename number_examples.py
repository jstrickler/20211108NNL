# we don't care: boolean complex

i1 = 1000     # 10
i2 = 0x1000   # 16
i3 = 0b1000   #  2
i4 = 0o1000   #  8
print(i1, i2, i3, i4)

x = 2395231303230486728578239582759285729357293587293857298357298375295923561961
print(x + 1)

f1 = 123.45
f2 = 10.
f3 = 0.0
f4 = .8293
f5 = 1.323e12
print(f1, f2, f3, f4, f5)

a = 23
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # true division
print(a // b) # floored division (round down to nearest whole number)
print(a // -b)
print(a ** b)
print(a % b)  # modulus (remainder)
x = a / b
print(x)

# PEMDAS

m = 5
m += 15  # m = m + 15
#  VAR op= VALUE   ==>   VAR = VAR op VALUE
m *= 3
m //= 10
print(m)

x = 10
x += 1
print(x)



