import numpy as np
import pandas as pd

age = np.random.randint(18,61,(100,1))
salary = np.random.randint(30000,100000,(100,1))
experience = np.random.randint(0,21,(100,1))
score = np.random.rand(100,1)
bias = np.ones((100,1))

data = np.hstack((age, salary, experience, score, bias))

df = pd.DataFrame(data, columns=["Age","Salary","Experience","Score","Bias"])

print(df)