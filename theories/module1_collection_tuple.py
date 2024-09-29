house1 = 'прихожия', 'ванна-туалет'
house2 = tuple(['прихожия', 'ванна-туалет'])
house = ('прихожия', 'ванна-туалет')
print(house)

print(house[0])
# error
# house[0] = "большая прихожия"

house = ('прихожия', ['ванна', 'туалет'])
print(house)
house[1][0] = 'туалет'
print(house)
house[1].remove('туалет')
print(house)
