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

def char_frequency(text):
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1   # 없으면 0에서, 있으면 기존값에서 +1
    return freq
"""
get 명령어의 사용법 -> dictionary.get(ch) => 기본적으로 없으면 None을 반환하지만 실제로 우리가 원하는는건 없으면 "0"을 반환하는것
그러니깐 get(ch, 0) 이렇게 하면 없으면 None이 아니라 0을 반환한다
"""