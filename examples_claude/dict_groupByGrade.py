def groupByGrade(grades):
    res = {}
    for student, grade in grades.items():
        res[grade] = res.get(grade, []) + [student]
    return res