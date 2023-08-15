import numpy as np

# Set the mean of the exponential distribution
mean = 20
sum = 0

for size in range(1, 10):
    for i in range(0, 1000000):
        # Generate 10 exponential random numbers
        random_numbers = np.random.exponential(scale=mean, size=size)

        # Find the maximum of the generated numbers
        maximum = np.max(random_numbers)
        sum += maximum

    sum /= 1000000
    print("Maximum of the generated numbers:", sum)


