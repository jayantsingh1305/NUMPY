import numpy as np

data = np.array([
    [1,200,0],
    [2,300,1],
    [3,400,0],
    [4,500,1]
])

features = data[:, :2].copy()
target = data[:,2]

features = features/np.max(features, axis=0)

features[:, 0] = features[:, 0]*10

print("Original Date:\n", data)
print("Processed Features:\n", features)
print("Target:\n", target)