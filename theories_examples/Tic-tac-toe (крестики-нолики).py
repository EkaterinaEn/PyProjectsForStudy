
def draw_area():
    for i in area:
        print(*i)
    print()


area = [["*", "*", "*"],["*", "*", "*"],["*", "*", "*"]]
print('Добро пожаловать в крестики-нолики')
print("------------------------------")
draw_area()
row = int(input("Введите номер строки (1,2,3) "))-1
column = int(input("Введите номер столбца (1,2,3) "))-1
# area[0][0] = "X"
draw_area()