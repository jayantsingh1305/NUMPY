import numpy as np

X = np.array([[1,3],[2,5],[4,6],[6,8]])
W = np.array([[2],[4]])

b = 5

Y = X @ W + b
print(Y)