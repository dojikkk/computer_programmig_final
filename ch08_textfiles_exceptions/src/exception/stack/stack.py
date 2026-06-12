'''
Stack module.

Implements a stack data structure.
Function getStack() creates and returns an empty stack. All other
functions receive a stack as input to perform their operation.
'''


def getStack():
    '''Create and return empty stack'''
    return []


def isEmpty(s):
    '''Return True if stack empty, otherwise False'''
    if s == []:
        return True
    else:
        return False


def top(s):
    '''
    Return the top item of stack, item not removed.
    Otherwise, raise ValueError exception.
    '''
    if isEmpty(s):
        # return None
        raise ValueError('stack is empty!')
    else:
        return s[len(s) - 1]


def push(s, item):
    '''Push item onto the top of stack'''
    s.append(item)


def pop(s):
    '''
    Remove and return top item of stack.
    If stack empty, raise ValueError exception.
    '''
    if isEmpty(s):
        # return None
        raise ValueError('stack is empty!')
    else:
        item = s[len(s) - 1]
        del s[len(s) - 1]
        return item


def pop2(s):
    '''
    Strictly speaking, above pop() function duplicates
    the code of the top() function.

    The pop2() function realizes the pop functionality by using top(). A
    ValueError exception raised in top() will propagate here, without being
    handled, thus propagated further to the caller of pop2().
    '''
    t = top(s)  # Will result in ValueError exception if empty stack.

    # We will reach here only if stack was not empty. Otherwise,
    # the ValueError exception will have taken us back to the caller of pop2()
    # already.
    del s[len(s) - 1]
    return t
