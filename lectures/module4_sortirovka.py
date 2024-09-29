nums = [5, 6, 2, 1, 3, 4]

def bubble_sort(ls):
    swapped = True # следит за тем происходили ли перестановки элементов во время текущей итерации
    while swapped:
        swapped = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i+1]:
                ls[i], ls[i+1] = ls[i+1], ls[i]
                swapped = True # позволит нам перейти на следующую итерацию


# bubble_sort(nums)
# print(nums)

def selection_sort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
                ls[i], ls[lowest] = ls[lowest], ls[i]


selection_sort(nums)
print(nums)