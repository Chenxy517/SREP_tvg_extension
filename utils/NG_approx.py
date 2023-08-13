
ana = []
p = 0.05
q = 1 - p

k = 5
for n in range(1, 20):
    u = 1
    for x in range(0, k):
        u *= (1 - ((1 - q ** x) ** n))
    u += n * (q ** k) / p
    ana.append(u)

print(ana*2)
