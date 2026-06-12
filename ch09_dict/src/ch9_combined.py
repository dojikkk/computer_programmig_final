#
# Multiple lists to store student information:
#


# def getGrade(student, name_list, grade_list,
#              course_list):
#     i = name_list.index(student)
#     grade = grade_list[i]
#     course = course_list[i]
#     return (grade, course)
#
#
# names = ['Jiin', 'Jinoo', 'Ana']
# grades = ['A+', 'B', 'A0']
# courses = ['2100', '2102', '3100']
#
# x = getGrade('Jinoo', names, grades, courses)
# print(x)


#
# Dictionary to store student grades:
#
# grades = {'Jiin': 'A+', 'Jinoo': 'B', 'Ana': 'A0'}
# print(grades['Jiin'])
# # grades['Carl']  # raises KeyError exception
# grades['Carl'] = 'A+'
# print(grades['Carl'])
# del grades['Jiin']
# print(grades)
# print(grades.keys())
# for person in grades.keys():
#     print(person)
# for grade in grades.values():
#     print(grade)
