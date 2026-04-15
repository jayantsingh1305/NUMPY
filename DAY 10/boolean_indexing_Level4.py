import numpy as np

marks = np.array([35, 80, 90, 20, 60, 45, 77, 88, 55])
attendance = np.array([60, 90, 85, 50, 70, 65, 80, 95, 40])

print("Student Who Passed", marks[marks>=40])
print("------")
print("Distinction", marks[marks>=40])
print("------")
print("Scholarship Student", marks[(marks>=75) & (attendance>=80)])