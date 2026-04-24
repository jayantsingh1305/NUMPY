import numpy as np

X = np.array([[1,2],[3,4],[5,6]])
W = np.array([[2],[1]])

Y=X@W
print(Y)
print(Y.shape)

print("------")

A = np.array([[1,2,3]])
B = np.array([[4],[5],[6]])

print(A@B)

print("------")

X = np.array([[2,1],[0,3]])
W = np.array([[1],[2]])

Y = X @ W
print(Y)