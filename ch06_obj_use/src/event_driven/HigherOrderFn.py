import math


def cco1100(f, x):
    """ 
    Higher-order function returning the result of
    calling function f with argument x.
    """ 
    return f(x)


m = cco1100(abs, -2)
n = cco1100(math.factorial, 3)
o = cco1100(print, -2)
p = cco1100(input, 'Enter a number: ')
print(m, n, o, p)
