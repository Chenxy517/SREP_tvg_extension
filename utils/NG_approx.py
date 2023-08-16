import math
import scipy.special
import scipy.constants
import numpy as np

def lq(x, q):
    return np.log(x) / np.log(1/q)

def four(k, q):
    Q = 1/q
    logQ = np.log(Q)
    numerator = -1 / (logQ)
    argument = -2 * k * np.pi * 1j / logQ
    gamma_term = scipy.special.loggamma(argument)
    result = numerator * gamma_term
    return result
    
p = 0.05
q = 1-p
N = 2

approx = []

for b in range(1, 11):
    x = lq(N, q) + (b-1)*lq(lq(N, q), q) + (b-1)*lq(p,q) + (b-1) - lq(math.factorial(b - 1), q)
    E_nb = x + 0.5 + (0.57721566490153286060651209)/lq(1/q, q)
    approx.append(E_nb)

print(approx)

print(lq(lq(N,q),q))