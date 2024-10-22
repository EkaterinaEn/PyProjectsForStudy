class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if not isinstance(other, House):
            return False
        return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
        if not isinstance(value, int):
            return
        self.number_of_floors = self.number_of_floors + value
        return self

    def __iadd__(self, value):
        return self + value

    def __radd__(self, value):
        return self + value

    def __gt__(self, other):
        if not isinstance(other, House):
            return False
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if not isinstance(other, House):
            return False
        return self.number_of_floors >= other.number_of_floors

    def __lt__(self, other):
        if not isinstance(other, House):
            return False
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if not isinstance(other, House):
            return False
        return self.number_of_floors <= other.number_of_floors

    def __ne__(self, other):
        if not isinstance(other, House):
            return False
        return self.number_of_floors != other.number_of_floors



h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__