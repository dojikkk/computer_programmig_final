import stack

st = stack.getStack()

for item in range(1, 5):
    stack.push(st, item)

# for item in range(1, 5):
#    st.append(item) # bad practice (see lecture slides!)

while not stack.isEmpty(st):
    item = stack.pop(st)
    print(item)
