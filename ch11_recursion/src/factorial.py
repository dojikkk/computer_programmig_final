"""
Program to demonstrate the recursive computation of the factorial function.
"""


def fact(n):
    """
    Compute the value of the factorial function for argument n,
    commonly written as n!

    Precondition:  n >= 1
    """
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print('fact(4) =', fact(4))
