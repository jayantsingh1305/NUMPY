import numpy as np

# A = np.array([[1,2],[3,4]])
# B = np.array([[5,6],[7,8]])

# print(A)
# print(B)

# A = np.array([[2,4],[6,8]])
# B = np.array([[1,3],[5,7]])

# print(A+B)
# print(A-B)
# print(A*B)
# print(A@B==B@A)

X=np.array([[1,2],[3,4]])
W=np.array([[2],[1]])

Y = X@W
print(Y)