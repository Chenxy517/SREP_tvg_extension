import math
import scipy.special
import scipy.constants
import numpy as np

def lq(x, q):
    return np.log(x) / np.log(1/q)

def F_fourier_coefficient(k, q):
    Q = 1/q
    return -1 / (np.log(Q)) * (1 / (2 * k * np.pi * 1j)) *scipy.special.loggamma(-2 * k * np.pi * 1j / np.log(Q))

def F(x, q, num_terms=50):
    Q = 1/q
    F_value = 0
    for k in range(-num_terms, num_terms + 1):
        if k != 0:
            F_value += F_fourier_coefficient(k, q) * np.exp(2j * np.pi * k * x)
    return F_value
    
p = 0.05
q = 1-p
N = 2

approx = []

for b in range(1, 11):
    x = lq(N, q) + (b-1)*lq(lq(N, q), q) + (b-1)*lq(p,q) + (b-1) - lq(math.factorial(b-1), q)
    E_nb = x + 0.5 + (0.57721566490153286060651209)/lq(1/q, q) + F(x, q)
    approx.append(E_nb)

print(approx)

print(lq(lq(N,q),q))