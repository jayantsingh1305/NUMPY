import numpy as np

# Columns: [Age, Math Marks, Science Marks]
data = np.array([
    [18, 85, 78],   # Student 1
    [19, 92, 88],   # Student 2
    [17, 76, 95],   # Student 3
    [18, 65, 70],   # Student 4
    [20, 90, 85]    # Student 5
])

#Get the shape of the matrix
print(data.shape)

#Find the average age of students
print(np.mean(data[:,0]))

#Extract Math Marks of all students
print(data[:,1])

#Find the highest science marks
print(np.max(data[:3]))