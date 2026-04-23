import numpy as np

# arr = np.array([1,2,3])
# b = arr
# b[0] = 100

# print(arr)

# arr = np.array([10, 20, 30])
# view_arr = arr.view()

# view_arr[1] = 999

# print(arr)

arr = np.array([5,6,7])
copy_arr = arr.copy()

copy_arr[2] = 500
print(arr)