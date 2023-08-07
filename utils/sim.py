import numpy as np

def find_bigger(element, subsequent_array):
    for item in subsequent_array:
        if item > element:
            return item

def sim():
    stamp_arr = []
    array_size = 20
    mean_interval = 20
    for i in range (2):
        array = np.cumsum(np.random.exponential(scale=mean_interval, size=array_size))
        stamp_arr.append(array)
    
    start_1 = stamp_arr[0][0]
    result_1 = find_bigger(start_1, stamp_arr[1])

    start_2 = stamp_arr[1][0]
    result_2 = find_bigger(start_2, stamp_arr[0])   
    return max(result_1, result_2)

result = []
for i in range(100000):
    result.append(sim())

print("Result: ", np.mean(result))