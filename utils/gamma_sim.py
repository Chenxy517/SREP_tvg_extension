import numpy as np

# Parameters for the Gamma distribution
k = 24
theta = 20

# Number of samples to generate
num_samples = 100000

# Generate random samples from the Gamma distribution
sample_1 = np.random.gamma(k, scale=theta, size=num_samples)
sample_2 = np.random.gamma(k, scale=theta, size=num_samples)

# Calculate the maximum of the two samples element-wise
max_sample = np.maximum(sample_1, sample_2)

# Display some statistics
print("Mean 1:", np.mean(sample_1))
print("Mean 2:", np.mean(sample_2))
print("Mean of the maximum:", np.mean(max_sample))
