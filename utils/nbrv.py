import numpy as np

# Parameters
gamma_list = [14, 19]
p = 0.05
size = 10000  # Number of samples to generate
ana = []

for gamma in gamma_list:
    # Generate negative binomial random variables
    variable1 = np.random.negative_binomial(gamma, p, size)
    variable2 = np.random.negative_binomial(gamma, p, size)

    # Calculate the maximum of the two variables
    max_value = np.maximum(variable1, variable2)

    ana.append(2 * np.mean(max_value))

print(ana)