house = ['entranceHall', 'toilet', 'bathroom', 'bedroom']
print(house)

is_work = True
i = 0
while is_work:
    print(house[i])
    i = i + 1
    if i == len(house):
        is_work = False
