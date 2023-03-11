e = 53
phi_n = 300
d = 1
while (e*d) % phi_n != 1:
    d += 1
print(d)

n = 341
d = 197
Z = 7
M = pow(Z, d, n)
print(M)
