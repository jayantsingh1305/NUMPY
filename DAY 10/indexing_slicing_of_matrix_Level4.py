import numpy as np

dataset = np.array([
    [101,25,50000,1],
    [102,30,60000,0],
    [103,35,70000,1],
    [104,40,80000,0],
    [105,45,90000,1]
])

print(dataset)
print("------")
print(dataset[:,1:])
print("------")
print(dataset[:,1:3])
print("------")
print(dataset[:,-1:])
print("------")