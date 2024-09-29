def recFunction(number):
    if number > 0 :
        print(number)
        return recFunction(number - 1)
    else:
        return str(number)

recFunction(5)
