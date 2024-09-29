house = ['прихожия', 'ванна-туалет']
print(house)

print(house[0])
house[0] = "большая прихожия"
print(house[0])

house.append('спальня')
house.append('кухня')
house.append('балкон')
print(house)
house.remove('балкон')
print(house)