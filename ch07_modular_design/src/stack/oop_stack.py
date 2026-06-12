'''
   Stack module.

   Implements a stack data-structure as a Python class.
   At this stage, we have not studied object orientation. Thus the
   details of this Python class do not concern us yet. We only want
   to note that a stack object has the methods provided with the
   class:
     __init__()
     isEmpty()
     top()
     push()
     pop()
'''


class Stack:

    def __init__(self):
        '''Create and return an empty stack object.'''
        self.s = []

    def isEmpty(self):
        '''Return True if stack empty, otherwise return False'''
        if self.s == []:
            return True
        else:
            return False

    def top(self):
        '''
        Return the top item of stack without removing.
        Return None if stack is empty.
        '''
        if self.isEmpty():
            return None
        else:
            return self.s[len(self.s) - 1]

    def push(self, item):
        '''Push item on the top of the stack.'''
        self.s.append(item)

    def pop(self):
        '''
        Remove and return top item from stack.
        If stack is empty, return None.
        '''
        if self.isEmpty():
            # early exit from pop() for empty stack:
            return None
        # if we come here, stack is not empty:
        item = self.s[len(self.s) - 1]
        del self.s[len(self.s) - 1]
        return item
