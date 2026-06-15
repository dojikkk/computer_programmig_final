class Member:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Student(Member):
    def __init__(self, name, student_id):
        Member.__init__(self, name)
        self.student_id = student_id
    def __str__(self):
        return f"{self.name} ({self.student_id})"

class Club:
    def __init__(self, title):
        self.title = title
        self.members = []
    def add(self, person):
        if not isinstance(person, Member):
            raise TypeError
        elif person in self.members:
            raise ValueError
        else:
            self.members.append(person)

    # 마지막 반환시 주의하기, 저게 단순한 객체 자체를 반환하는건지 객체에 메소드를 씌워서 name 형태를 반환해야하는건지 잘 구분해주기
    def student_names(self):
        return [x.name for x in self.members if type(x) == Student]
    def all_names(self):
        return [x.name for x in self.members]