#name = input('Как тебя зовут?')
#print(f'Здравствуйте, {name}')
# first = 'Вторник'
# second = 'Понедельник'
# print(f'{second}, {first}')
# a = 5
# b = 10
# c = 10
#if a>b:
    #print('a больше чем b')
#if b>a:
    #print('b больше чем а')
#a = 5
#b = 10
#c = 10
#if a==b or a==c or b==c:
    #print(2)
#elif a==b==c:
    #print(3)
#else:
    #print(0)
# a = []
# a.append('a')
# print(a)
# grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# grades_k = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]
# print(grades_k)
# students_sort = sorted(students)
# print(students_sort)
# # dict1 = dict(zip(students_sort,grades_k))
# dict1 = {students_sort[0]:grades_k[0], students_sort[1]:grades_k[1]}
# print(dict1)
# *args - распаковка(запаковка) позиционных параметров, содержащих один элемент (списки, кортеджи, множества)
#**kwargs распаковка(запаковка) именнованных параметров, содержащих пару элементов (словари)
def print_params(**kwargs):
    print(kwargs)

# list_= [1, 2, 3]
dict_ = {'a': 1, 'b': 2, 'c': 3}
print_params(**dict_)
