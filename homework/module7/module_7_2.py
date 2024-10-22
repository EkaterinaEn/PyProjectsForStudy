
def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    for i in range(0, strings.__len__()):
        byte_number = file.tell()
        file.write(strings[i] + '\n')
        strings_positions.update({(i+1, byte_number) : strings[i]})
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

value_strings_positions = custom_write("test.txt", info)
#print(value_strings_positions)
for key, value in value_strings_positions.items():
    print(key, "  ", value)