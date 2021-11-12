cities = list()   # cities is *instance* of the *list* class
d1 = dict()
cities.append('Durham')
cities.append('Albany')
print(cities)

# append_to_list(cities, 'Durham')

x = 5    #   x = int(5)
print(type(cities), type(x))
print(x.real)

cities.insert(0, 'Tampa')
print(cities)   #   print(str(cities))   #  print(cities.__str__())

class Dog:
    def bark(self):
        print("Woof! Woof!")

d1 = Dog()
d2 = Dog()
d3 = Dog()
d1.bark()
d2.bark()

# "callable"
#  function class
