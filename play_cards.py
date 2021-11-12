##
from carddeck import CardDeck, JokerDeck
##
# client code

d1 = CardDeck("Abigail")
print(d1)
d2 = CardDeck("Phryne")

# BAD:
print(d1._dealer)  # "real" data

# GOOD:
print(d1.dealer)  # property  "view"

d1.dealer = "Flynn"
print(d1.dealer)

for name in 123.456, ['foo'], 'Bob':
    try:
        d1.dealer = name
    except TypeError as err:
        print(err)
    else:
        print(d1.dealer)

try:
    dd = CardDeck(0.9)
except TypeError as err:
    print(err)
else:
    print(dd)

d1.shuffle()
print(d1.cards, '\n')

for _ in range(5):
    c = d1.draw()
    print(c)  # print(str(c))
#    print(c.rank, c.suit)
print()

# len()

print(len(d1), len(d2))
print(d1)
print(d2)
##
print(repr(d1))
print(repr(d2))
##
print(d1.get_ranks())
print(CardDeck.get_ranks())
##
j = JokerDeck('Albert')
print(j)
j.shuffle()
##

##
print(j.draw())
print(j.cards)
##



