import numpy as np


array_size = 10
mean_interval = 10
interval = []
for i in range (10000):
    array = np.cumsum(np.random.exponential(scale=mean_interval, size=array_size))
    interval.append(array[3] - array[1])

print("Mean Interval:", np.mean(interval))