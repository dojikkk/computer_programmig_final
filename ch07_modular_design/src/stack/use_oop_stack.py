from oop_stack import Stack  # import Stack class

st = Stack()  # create a Stack object

for item in range(1, 5):
    st.push(item)  # call method push() on stack object

while not st.isEmpty():
    item = st.pop()  # call method pop() on stack object
    print(item)
