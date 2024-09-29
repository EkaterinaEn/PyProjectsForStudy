grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades_s = [sum(grades[0])/len(grades[0]), sum(grades[1])/len(grades[1]), sum(grades[2])/len(grades[2]), sum(grades[3])/len(grades[3]), sum(grades[4])/len(grades[4])]
print(grades_s)
students_sort = sorted(students)
print(students_sort)
dict1 = {students_sort[0]:grades_s[0], students_sort[1]:grades_s[1], students_sort[2]:grades_s[2], students_sort[3]:grades_s[3], students_sort[4]:grades_s[4]}
print(dict1)