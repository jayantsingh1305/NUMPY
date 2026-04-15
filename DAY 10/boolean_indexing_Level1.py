import numpy as np

arr = np.array([10, 25, 30, 45, 50])

print(arr)
print("------")
print(arr[arr>30])
print("------")
print(arr[arr<=25])
print(arr[arr%10==0])