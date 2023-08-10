import numpy as np
import random

prob_con = 0.05
prob_discon = 1 - prob_con

means = []

# Generate 100000 samples
for i in range(100000):
    random_seed = random.randint(0, 2**32 - 1)
    # Set the random seed for NumPy
    np.random.seed(random_seed)
    bool_array = np.random.choice([True, False], size=2000, p=[prob_con, prob_discon])
    true_indices = np.where(bool_array)[0]
    
    # Append the mean of the true_indices to the means list
    if len(true_indices) > 0:
        means.append(true_indices[0])

# Calculate and print the mean of means
print("Mean:", np.mean(means))
