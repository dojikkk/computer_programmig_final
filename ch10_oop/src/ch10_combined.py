import datetime

#
# OOP stack sneak preview:
#


# class Stack:
#     def __init__(self):
#         self.s = []
#
#     def push(self, item):
#         self.s.append(item)
#         print('Pushed item', item, 'onto stack')
#
#
# st = Stack()
#
# st.push(0)
# st.push(1)
# st.push(2)


#
# Class with __init__ method:
#

# class Coordinate:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         print('__init__, x, y:', x, y)
#
#
# c = Coordinate(1, 2)
#
# origin = Coordinate(0, 0)


#
# Same class, distance method added:
#

# class Coordinate:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         # print('__init__, x, y:', x, y)
#
#     def distance(self, other):
#         x_diff = (self.x-other.x)**2
#         y_diff = (self.y-other.y)**2
#         return (x_diff + y_diff)**0.5
#
#
# c = Coordinate(1, 2)
#
# c = Coordinate(4, 3)
# orig = Coordinate(0, 0)
# d = c.distance(orig)
# print('distance:', d)
#
# # d = Coordinate.distance(c, orig)
# print('distance:', d)
#
# print(c)


#
# Same class, __str__ method added:
#

# class Coordinate:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def distance(self, other):
#         x_diff = (self.x-other.x)**2
#         y_diff = (self.y-other.y)**2
#         return (x_diff + y_diff)**0.5
#
#     def __str__(self):
#         return '<'+str(self.x)+','+str(self.y)+'>'
#
#
# c = Coordinate(4, 3)
# print(c)

#
# Fraction class:
#


# class Fraction(object):
#     """
#     Class to represent a number as a fraction
#     """
#
#     def __init__(self, n, d):
#         """ Method to construct a Fraction object """
#         # Check that n and d are of type int:
#         if type(n) != int or type(d) != int:
#             raise ValueError('requires type int')
#         # Check that denominator is non-zero:
#         if d == 0:
#             raise ZeroDivisionError('requires non-zero denominator')
#         # If we get here, n and d are ok => initialize Fraction:
#         self.num = n
#         self.denom = d
#
#     def __str__(self):
#         """ Return a string representation of the fraction object (self) """
#         return str(self.num) + '/' + str(self.denom)
#
#     def __mul__(self, other):
#         """ Return new Fraction representing self * other """
#         new_num = self.num * other.num
#         new_denom = self.denom * other.denom
#         return Fraction(new_num, new_denom)
#
#     def __add__(self, other):
#         """ Return new Fraction representing self + other """
#         new_num = self.num * other.denom + other.num * self.denom
#         new_denom = self.denom * other.denom
#         return Fraction(new_num, new_denom)
#
#     def __float__(self):
#         """ Return a float value of the Fraction object"""
#         return self.num / self.denom  # result of / is of type float
#
#
# x = Fraction(1, 2)
# y = Fraction(3, 4)
# z = x * y                    # infix notation, z is a Fraction object
# z1 = x.__mul__(y)            # equivalent (object.method(other_object))
# z2 = Fraction.__mul__(x, y)  # equivalent (class.method(obj1, obj2))
# print(z, z1, z2)
# print(z.__float__())
# print(float(z))
# # k = Fraction(0.5, 5) # exception ValueError
# # k = Fraction(1,0)    # exception ZeroDivisionError


#
# Public attributes versus properties:
#

# class A:
#
#    def __init__(self, val):
#        self.x = val
#
#
# m = A(20)
# print(m.x)


# class B:
#
#     def __init__(self, val):
#         self.x = val
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, val):
#         if val < 0:
#             self.__x = 0
#         elif val > 100:
#             self.__x = 100
#         else:
#             self.__x = val
#
#
# n = B(20)
# print(n.x)
# n.x = -1
# print(n.x)


#
# Person class hierarchy:
#


# class Person(object):
#     """
#     Class to represent a person.
#     Attributes: name, birthday
#     """
#
#     def __init__(self, name):
#         """ Create a person with name 'name' """
#         self.name = name
#         self.birthday = None
#
#     def getName(self):
#         """ Return person's name """
#         return self.name
#
#     def setBirthday(self, birthDate):
#         """
#         Set person's birthday. Assumes 'birthDate' is of type
#         datetime.date. Throws ValueError otherwise.
#         """
#         if type(birthDate) != datetime.date:
#             raise ValueError("require birthday of type datetime.date")
#         self.birthday = birthDate
#
#     def getAge(self):
#         """
#         Assume that self's birthday has been set.
#         Return self's current age in days.
#         """
#         if self.birthday is None:
#             raise ValueError("Birthday not set")
#         return (datetime.date.today() - self.birthday).days
#
#     def __str__(self):
#         """ Provide self's representation as a str """
#         return self.name


# p1 = Person('Seongho Ahn')
# p2 = Person('Yousun Park')
# p1.setBirthday(datetime.date(1991, 3, 22))
# #p2.setBirthday(1991) # exception ValueError (not a date object!)
# print(p1.getAge(), 'days old')
# #print(p2.getAge())    # exception ValueError (birthday not set!)


# class YonseiPerson(Person):
#     """
#     YonseiPerson is a descendant of class Person.
#     A YonseiPerson has an ID value.
#     """
#
#     def __init__(self, name, ID):
#         """ Create a YonseiPerson of ``name'' and ''ID'' """
#         # Initialize data attributes inherited from parent class:
#         Person.__init__(self, name)
#         # Initialize own data attribute:
#         self.ID = ID
#
#     def getID(self):
#         """ Return the ID of a YonseiPerson object """
#         return self.ID
#
#     def __str__(self):
#         """ Provide self's representation as a str """
#         return "YU's " + self.name + ' (ID ' + str(self.ID) + ')'


# SPark = YonseiPerson('Susan Park', 7003)
# print(SPark.getID())
# print(SPark)
# NoYU = Person('Peter Neumann')
# #NoYU.getID() # ouch! Person class does not have getID() method


# class Employee(Person):
#     """Employee is a descendant of class Person.
#        An employee has a department and a salary."""
#
#     def __init__(self, name, dept, salary):
#         Person.__init__(self, name)
#         self.dept = dept
#         self.salary = salary
#
#     def getDepartment(self):
#         return self.dept
#
#     def getSalary(self):
#         return self.salary


# class PersonList(object):
#     """
#     PersonList is a list object to store Person objects
#     and all subclasses thereof.
#     """
#
#     def __init__(self, listname):
#         """ Initialize the PersonList to the empty list and set it's name """
#         self.listname = listname
#         self.persons = []
#
#     def addPerson(self, candidate):
#         """
#         Add an object to the PersonList. Objects of class-types
#         which are not descendants of class Person will be
#         rejected. Duplicates will be rejected, too.
#         """
#         if not isinstance(candidate, Person):
#             raise TypeError('Not a person type')
#         if candidate in self.persons:
#             raise ValueError('Duplicate person')
#         self.persons.append(candidate)
#
#     def removePerson(self, candidate):
#         """ Remove an object from the list """
#         try:
#             self.persons.remove(candidate)
#         except ValueError:
#             print(str(candidate) + ' not in ' + self.listname)
#
#     def getYonseiPersons(self):
#         """
#         Return a list of names of all YonseiPersons
#         """
#         ps = []
#         for p in self.persons:
#             if type(p) == YonseiPerson:
#                 ps.append(p.getName())
#         return ps
#
#     def getAllPersons(self):
#         """ Return a list of names of all persons contained """
#         ps = []
#         for p in self.persons:
#             ps.append(p.getName())
#         return ps


# p1 = YonseiPerson('Shinhyung Yang', 1)
# p2 = YonseiPerson('P. Tuthill', 2)
# p3 = Person('Peter Pan')
# p4 = Employee('Jinwoo Park', 'LG mobile', 45000)
# l = PersonList('mylist')
# #l.addPerson(22) #ouch: 22 not a Person type
# l.addPerson(p1)
# l.addPerson(p2)
# l.addPerson(p3)
# l.addPerson(p4)
# #l.addPerson(p4) #ouch: duplicate person
#
# print(l.getYonseiPersons())
# print(l.getAllPersons())
