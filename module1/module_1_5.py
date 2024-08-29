immutable_var = 1, 2, 3, True, 'Ekaterina'
print(immutable_var)
#immutable_var[5] = 'Sofia'
#print(immutable_var) кортеж не поддерживает обращение по элементам
mutable_list = ['межевой план', 'кадастровый план', 'акт обследования']
print(mutable_list)
mutable_list[1] = 'технический план'
print(mutable_list)
mutable_list.append(True)
print(mutable_list)
mutable_list.extend('False')
print(mutable_list)
mutable_list.extend(['False', 5])
print(mutable_list)
mutable_list.remove('акт обследования')
print(mutable_list)
print('межевой план' in mutable_list)
print('межевой план' not in mutable_list)
print(mutable_list[0:2:2])


