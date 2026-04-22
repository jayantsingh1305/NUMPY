import numpy as np

# arr = np.array([1,2,3,4])

# view_arr = arr.view()
# copy_arr = arr.copy()
# arr[0] = 100

# print("Original :",arr)
# print("View :",view_arr)
# print("Copy :",copy_arr)

# arr = np.array([10,20,30])
# b = arr
# b[1] = 999
# print(arr)

# arr = np.array([1,2,3])
# view = arr.view()
# view[2] = 50
# print(arr)

arr = np.array([5,6,7])
copy = arr.copy()
copy[0] = 100
print(arr)