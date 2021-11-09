actor = "Chris Hemsworth"

print(len(actor), type(actor))  # len() and type() are *builtin* functions

print(actor.upper())
a = actor.upper()
print(a)

print("foo" + "bar")
print("-" * 60)
print("Python" * 3)

print(actor)
print(actor.count('h'))
print(actor.lower().count('h'))
print("spam".upper())
print(actor.startswith('Chris'))
print(actor.startswith('Liam'))
print("worth" in actor)
print("value" in actor)
print(actor)
print(actor.find('worth'))
print(actor.find('value'))

s = "        All my exes live in Texas        "
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()

s1 = "xxxxxxxxyxxxxxxxyxyxAll my exes live in Texasxyyyyyyyyyyyyyyxyyyyyyyyyyxyxyy"
print("|" + s1.lstrip("xy") + "|")
print("|" + s1.rstrip("xy") + "|")
print("|" + s1.strip("xy") + "|")
print()

print(s.split())
words = s.split()
print(words)
print("/".join(words))
print(", ".join(words))

s = "fee_fi_fo_fum"
print(s.split("_"))

s = "alpha, beta, gamma"
print(s.split(', '))

s = 'one,two three, four'

# see chapter 12 ...
import re
print(re.split('[,\s]+', s))


