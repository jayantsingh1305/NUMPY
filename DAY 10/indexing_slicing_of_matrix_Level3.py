import numpy as np

data = np.array([
    [25, 50000, 1],
    [30, 60000, 0],
    [35, 70000, 1],
    [40, 80000, 0]
])

print(data)
print("------")
print(data[:,0:2])
print("------")
print(data[:,-1:])
print("------")
print(data[0:3,0:3])
print("------")
print(data[:,1:2])