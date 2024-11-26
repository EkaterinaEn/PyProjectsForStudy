print("========== dict =================================")
house_dict = dict()
house_dict.update({'entranceHall': 10, 'toilet': 2, 'bathroom': 7, 'bedroom': 10})
print(house_dict)
print(house_dict['entranceHall'])

# error
# print(house_dict['balcony'])
print("кв м : ", house_dict.get('balcony'))
print("кв м : ", house_dict.get('bathroom'))
print(house_dict.get('balcony', 'в доме нет такого'))

house_dict.update({'entranceHall' : 10, 'bedroom': 15})
print(house_dict)

house_dict['balcony'] = 4
print(house_dict)
house_dict['balcony'] = 5
print(house_dict)

# удаление
balcony = house_dict.pop('balcony')
print("Удаленный: ", balcony, "квм")
print(house_dict)

for key, value in house_dict.items():
    print(key, value)


print("========== set =================================")

house_set = {'entranceHall', 'toilet', 'toilet','bedroom'}
print(house_set)
house_set.add('bathroom')
print(house_set)
# если элемента нет, будет ошибка
house_set.remove('bathroom')
print(house_set)
# если элемента нет, ошибки не будет
house_set.discard('bathroom')
print(house_set)

