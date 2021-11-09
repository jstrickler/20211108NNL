x = "123"
print(x * 3)
y = int(x)
print(y * 3)
print(int(x) * 3)

# str(obj)  bool(obj)

# int(str-or-number)  float(str-or-number)

a = "123"
b = 456
print(a + str(b))
print(int(a) + b)

x = "-100"
print(int(x))

sn = "1.233e18"
print(float(sn))

m = "1.46"
print(int(float(m)))

print(round(float(m), 1))

e = "       47      "
print(int(e, 10) * 10)

x = "DeadBeef"
print(int(x, 16))

value = "10101001101"
print(int(value, 2))

i  = 1234
print(bin(i), hex(i), oct(i))




