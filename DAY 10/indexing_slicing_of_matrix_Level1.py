import numpy as np

arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

print(arr[1:2,1:2])
print("------")
print(arr[0:1,:])
print("------")
print(arr[:,2:3])