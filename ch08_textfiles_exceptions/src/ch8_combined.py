# The os module allows us to use functionality provided by the underlying
# operating system:
import os

#
# Writing a file:
#

# print('Your file will be stored in directory', os.getcwd())
#
# fruits = open('fruits.txt', 'w')
# fruits.write('Apples\n')
# print('file-pointer position:', fruits.tell())
# fruits.write('Mangos\n')
# fruits.close()


#
# Reading a file:
#

# Case 1: read file using readline() statements:
# fruits = open('fruits.txt', 'r')
# print('file-pointer position:', fruits.tell())
# line_1 = fruits.readline()
# print(line_1)
# print('file-pointer position:', fruits.tell())
# line_2 = fruits.readline()
# print(line_2)
# print('file-pointer position:', fruits.tell())
# fruits.close()

# Case 2: read file from while-loop:
# fruits = open('fruits.txt', 'r')
#
# line = fruits.readline()
# while line != '':
#     print(line[:-1])
#     line = fruits.readline()
#
# fruits.close()

# Case 3: read file from for-loop:
# fruits = open('fruits.txt', 'r')
# for line in fruits:
#     print(line[:-1])
# fruits.close()


#
# Re-setting the file-pointer:
#

# fruits = open('fruits.txt', 'r')
# for line in fruits:
#     print(line[:-1])
# fruits.seek(0)
# for line in fruits:
#     print(line[:-1])
# fruits.close()


#
# Reading chunks of a specified size:
#

# fruits = open('fruits.txt', 'r')
# print('First chunk:', fruits.read(3), end='\n')  # read the first 3 characters
# print('Second chunk:', fruits.read(2), end='\n')  # read the next 2 characters
# print('Third chunk:', fruits.read(), end='@')  # read the remaining characters
# fruits.close()


#
# Setting UTF-8 as the text file encoding:
#

# f = open('testfile.txt', 'w', encoding='utf-8')
# f.write('öabc')
# f.close()


#
# Object serialization/deserialization with JSON:
#

# import json

# x = [1, 'a string', -1.5, True]
# y = json.dumps(x)
# print(y)  # [1, "a string", -1.5, true]

# f = open('json.txt', 'w', encoding='utf-8')
# f.write(y)
# f.close()

# f = open('json.txt', 'r', encoding='utf-8')
# z = json.load(f)
# f.close()
# print(z)  # [1, 'a string', -1.5, True]
# print(type(z))


#
# Searching, dissecting and constructing strings:
#

# email = 's_park@naver.com'
# at_index = email.find('@')
# user = email[0:at_index]
# domain = email[at_index + 1:]
# print(user, domain)


#
# Unhandled ZeroDivision Exception:
#

# numSuccesses = 10
# numFailures = int(input('failures: '))
# ratio = numSuccesses / numFailures
# print('The success/failure ratio is', ratio)
# print('Now here')


#
# Handled ZeroDivision Exception:
#

# numSuccesses = 10
# numFailures = int(input('failures: '))
# try:
#     ratio = numSuccesses / numFailures
#     print('The success/failure ratio is', ratio)
# except ZeroDivisionError:
#     print('Division by zero exception occurred!')
#     print('ratio is undefined!')
# print('Now here')


#
# Handling specific exceptions:
#

# try:
#     x = int(input('First number: '))
#     y = int(input('Second number: '))
#     print('x/y = ', x/y)
#     print('x+y = ', x + y)
#     print(xyz)  # Name error
# except ValueError:
#     print('Could not convert to number.')
# except ZeroDivisionError:
#     print("Can't divide by zero.")
# except:
#     print('Something else went wrong.')
#
# print('Good bye...')


#
# Input-loop controlled by Boolean flag:
#

# ValidInput = False
# while not ValidInput:
#     val = input('Enter an integer: ')
#     try:
#         val = int(val)
#         ValidInput = True  # exit loop
#     except ValueError:
#         print(val, 'is not an integer')
#     print('end of loop body reached')
#
# print('The square of your number is', val**2)


#
# Input-loop abstracted away inside function:
# (To reduce code-bloat.)
#

# def readInt():
#     while True:
#         val = input('Enter an integer: ')
#         try:
#             val = int(val)
#             return val
#         except ValueError:
#             print(val, 'is not an integer')
#
#
# x = readInt()
# y = readInt()
# print(x**y)


#
# Polymorphic input function:
# (To reduce code bloat.)
#

# def readVal(valType, requestMsg, errorMsg):
#     while True:
#         val = input(requestMsg)
#         try:
#             val = valType(val)
#             return val
#         except ValueError:
#             print(val, errorMsg)
#
#
# x = readVal(int, 'Enter an integer: ', 'not an integer')
# y = readVal(float, 'Enter a float: ', 'not a float')
# print(x, y)


#
# Propagation of a raised exception:
#

# import math
#
#
# def poorRead():
#     return int(input('Enter an integer: '))
#
#
# def computeCircleArea():
#     r = poorRead()
#     area = r**2 * math.pi
#     print('Result:', area)
#
#
# print("Let's compute a circle's area")
# try:
#     computeCircleArea()
# except ValueError:
#     print('Invalid computation, good bye...')


#
# Throwing exception back to function caller:
#

# def getRatios(vec1, vec2):
#     """Assumes: vec1 and vec1 are lists of equal length of numbers
#        Returns: a list containing the meaningful values of
#                 vec1[i] / vec2[i]"""
#     ratios = []
#     for index in range(len(vec1)):
#         try:
#             ratios.append(vec1[index] / vec2[index])
#         except ZeroDivisionError:
#             ratios.append(float('nan'))  # nan = Not a Number
#         except:  # all other exceptions (default handler)
#             raise ValueError('getRatios bad arguments!')
#     return ratios
#
#
# l1 = [1.0, 2.0, 7.0, 6.0]
# l2 = [1.0, 2.0, 0.0, 3.0]
# try:
#     print(getRatios(l1, l2))
#     print(getRatios([], []))
#     print(getRatios([1, 2], [3]))
# except ValueError as msg:  # assign exception to 'msg' variable
#     print(msg)
#     print(type(msg))


#
# Creating and throwing an exception by ourselves:
#
# x = ValueError('hi, this is a ValueError exception')
# print(type(x))
# raise x
