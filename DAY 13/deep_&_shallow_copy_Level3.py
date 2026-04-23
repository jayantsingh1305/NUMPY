import numpy as np

# def normalize(data):
#     data = data/np.max(data)
#     return data

# X = np.array([10,20,30])
# X_norm = normalize(X)

# dataset = np.array([
#     [1,200,0],
#     [2,300,1],
#     [3,400,0]
# ])

# features = dataset[:, :2]
# features[0][0] = -999

data = np.array([1,2,3,4,5])

step1 = data.view()
step2 = step1
step3 = step2.copy()

step1[0] = 100
step2[1] = 200
step3[2] = 300