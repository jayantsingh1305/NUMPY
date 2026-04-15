import numpy as np

arr = np.array([12, 25, 37, 45, 52, 60])

print(arr[(arr>30)&(arr<60)])
print("------")
print(arr[(arr<20)|(arr>50)])