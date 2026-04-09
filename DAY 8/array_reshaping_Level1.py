import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr)
print("------")
new_arr = arr.reshape(2,3)
print(new_arr)
print("-----")
print(new_arr.shape)
print("------")
new_arr = np.arange(8)
new_arr1 = new_arr.reshape(6,-1)
print(new_arr1)