import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print(A+B)
print(A*B)
print(A@B)

print("------")

C = np.array([[1,2,3],[4,5,6]])
print(C.shape)

print("------")

D = np.array([[2,0],[1,3]])
print(D@D)