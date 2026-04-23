import numpy as np

arr = np.array([1,2,3,4])
slice_arr = arr[1:3]

slice_arr[0] = 100

print(slice_arr)