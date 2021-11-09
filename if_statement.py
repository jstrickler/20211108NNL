value = 56

if value > 75:
    print("koala")
    print("kangaroo")
    if value > 90:
        print("cane toad")
elif value > 50:  # else if
    print("platypus")
    print("kiwi")
else:
    print("wombat")
    print("wallaby")

print("Done.")

# numbers        0 is False, otherwise True
# containers     len(x) == 0 is False, otherwise True (str bytes list tuple dict set)
# None            False
# everything else    generally True unless specifically programmed
#
x = True
if x:
    print("spam")
else:
    print("ham")


#  C      x = A ? B : C
# Python  x = B if A else C

debug = False
color = 'red' if debug else 'blue'
print(color)

# == != > < >= <=    is

x = 5
y = x
print(x is y, x == 5)

#  and or not
# and   T if both operands are T
# or    T unless both operands are F
# not   F if T, T if F

m = 32
if x < 10 and m > 20:
    print("wahooooo")

file_name =  "wombats.txt"

if file_name.endswith('.txt') or file_name.endswith('.text'):
    print("text file")

actor = "Chris Hemsworth"
if "Liam" not in actor:
    print("whoa")





