import numpy as np

salary = np.array([25000, 40000, 55000, 70000, 30000, 90000])

print(salary[salary>50000])
print("------")
print(salary[(salary>30000)&(salary<80000)])
print("------")
Bonus = salary[salary>60000]+5000
print(Bonus)