def add_everything_up(a, b):
    try:
        if (isinstance(a, (int, float))) == True and (isinstance(b, (int, float))) == True:
            result = round(a + b, 3)
        else:
            result = a + b
        return result
    except TypeError:
        result = (str(a) + str(b))
        return result

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
