phone_book = {'Denis': 8888888888, 'Max': 77777777777}
print(phone_book)
print(phone_book['Denis'])
phone_book['Denis'] = 55555555555
phone_book['Ekaterina'] = 4444444
del phone_book['Denis']
print(phone_book)
phone_book.update({'Sasha': 222222222222, 'Alexey': 1111111111})
print(phone_book)
print(phone_book.get('Ekaterina', 'нет такого'))
a = phone_book.pop('Max')
print(phone_book)
print(a)
print("keys : ", phone_book.keys())
print("values : ", phone_book.values())
print("items : ", phone_book.items())
set_ = {1, 2, 3, 4, 4, 5, 6, 6}
print(set_)
list_ = [1,1,1,1,1,1,1,1,22,22,22,25,26,27,28]
