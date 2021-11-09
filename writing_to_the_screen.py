person = "Fred Flintstone"
city = "Bedrock"
value = 1.380938

print(person, city, value)
# print(print(person, city, value, sep="/"))
x = person +  city +  str(value)
print(x)
x = '&'.join([person, city, str(value)])
print(x)

print("---")
print(person, end=' ')
print(city, value)
print(person, city, value, sep="/")
print(person, city, value, sep="")
print()  # goes to new line
print("===")

print(person, "lives in", city)
print("{} lives in {}".format(person, city))
print("Value is {:.2f}".format(value))

print(f"{person} lives in {city}")  # 3.6 and later
print(f"Value is {value:.2f}")


