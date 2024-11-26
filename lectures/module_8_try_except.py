def divv1():
    # try:
    i = 0
    ret = 10 / i


# except:
#     print("деление на ноль")

def divv2():
    # try:
    divv1()


# except:
#     print("деление на ноль")


if __name__ == "__main__":
    try:
        divv2()
    except:
        print("qqqq")
