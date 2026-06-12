from stack import getStack, isEmpty, pop, push

st = getStack()

for item in range(1, 5):
    push(st, item)

# for item in range(1,5):
#     st.append(item)  # bad practice (see lecture slides!)

while not isEmpty(st):
    item = pop(st)
    print(item)
