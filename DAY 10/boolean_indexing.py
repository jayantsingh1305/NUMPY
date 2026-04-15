# import numpy as np

# arr = np.array([10,20,30,40,50])

# print(arr>25)
# print("------")
# print(arr[arr>25])
# print("------")
# print(arr[arr<30])

import numpy as np

# arr = np.array([5,10,15,20,25])
# print(arr[arr>15])

# arr = np.array([100,200,300,400])
# print(arr[arr<300])

marks = np.array([35,80,90,20,60,45])
print("Pass Students - ",marks[marks>40])
print("Distinction - ",marks[marks>75])
print("Fail Students - ",marks[marks<40])