# module less_simple:

def func1():
    print('func1 called') 


#
# Variable __name__ is provided by the Python interpreter:
#
print('Hello, my name is', __name__)

if __name__ == "__main__":
    print('I am running as the main module.')
    func1()
else:
    print('I am running as an imported module.')
    print('My name is', __name__)
