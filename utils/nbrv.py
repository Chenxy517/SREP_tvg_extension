import numpy as np

# Parameters
gamma_list = list(range(1,10))
p = 0.15
size = 10000  # Number of samples to generate
ana = []

for gamma_1 in gamma_list:
    for gamma_2 in range(gamma_1, gamma_1+2):
        # Generate negative binomial random variables
        variable1 = np.random.negative_binomial(gamma_1, p, size)
        variable2 = np.random.negative_binomial(gamma_2, p, size)

        # Calculate the maximum of the two variables
        max_value = np.maximum(variable1, variable2)

        ana.append(2 * np.mean(max_value)+2)

print(ana)