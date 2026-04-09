import numpy as np

sensor_data = np.arange(120)
new_data = sensor_data.reshape(10,3,4)
print(new_data)