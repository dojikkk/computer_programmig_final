'''
Stack module.

Stack data structure implementation using Python lists.
Function getStack() creates and returns an empty stack. All other
functions receive a stack as input to perform their operation.
'''


def getStack():
    '''Create and return an empty stack'''
    return []


def isEmpty(s):
    '''Return True if stack empty, otherwise return False'''
    if s == []:
        return True
    else:
        return False


def top(s):
    '''
    Return the top item of stack if not empty; Item not removed.
    Otherwise, return None.
    '''
    if isEmpty(s):
        return None
    else:
        return s[len(s) - 1]


def push(s, item):
    '''Push item onto the top of stack'''
    s.append(item)


def pop(s):
    '''
    Remove and return top item of stack.
    If stack empty, return None.
    '''
    if isEmpty(s):
        return None
    else:
        item = s[len(s) - 1]
        del s[len(s) - 1]
        return item
