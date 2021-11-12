
class UnknownKnightError(Exception):
    pass

class Knight:

    def __init__(self, name):
        self._name = name
        with open('../DATA/knights.txt') as knights_in:
            for line in knights_in:
                (name,title,color,quest,cmt) = line[:-1].split(":")
                if name == self._name:
                    self._title = title
                    self._color = color
                    self._quest = quest
                    self._comment = cmt
                    break
            else:
                raise UnknownKnightError("No such knight as '" + self._name + "'")   

    @property
    def name(self):
        return self._name
            
    @property
    def title(self):
        return self._title
            
    @property
    def favorite_color(self):
        return self._color
            
    @property
    def quest(self):
        return self._quest
            
    @property
    def comment(self):
        return self._comment
            

if __name__== "__main__":
    for name in 'Arthur', 'Bedevere', 'Wilbur', 'Robin', 'Randolph':
        try:
            k = Knight(name)
        except UnknownKnightError as e:
            print(e)
        else:
            print(k.name, k.favorite_color, k.comment, k.title)
