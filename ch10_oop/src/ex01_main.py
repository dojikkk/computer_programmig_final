from ex01_class import Tensor

v = Tensor([1, 2, 3]) # 1x3
w = Tensor([4, 5, 6]) # 1x3

# 2x3 matrix
A = Tensor([
    [1, 2, 3], 
    [4, 5, 6],
])

A2 = Tensor([
    [1, 2, 3], 
    [4, 5, 6],
])

# 3x2 matrix
B = Tensor([
    [1, 2], 
    [3, 4], 
    [5, 6],
])

print("v =", v)
print("w =", w)
print("A =", A)
print("B =", B)

print("\nElementwise operations")
print("A + A2 =", A + A2)
#print("A + B =", A + B)
print("v + w =", v + w)
print("v * 10 =", v * 10)
#print("A + 1 =", A + 1)


print("\nVector operations")
print("v dot w =", v.dot(w))
print("norm(v) =", v.norm())

print("\nMatrix-vector multiplication")
print("A @ v =", A @ v)

print("\nMatrix-matrix multiplication")
print("A @ B =", A @ B)

print("\nTranspose")
print("A.T =", A.T)