p = 37
g = 2
gx = 15
gy = 29

y = 1
while pow(g, y, p) != gy:
    y += 1
print('y =', y)

p = 37
x = 13
gx = 15
gy = 29
y = 25

M = (gy**x * pow(gx, -y, p)) % p
print('M =', M)

p = 37
g = 2
x = 13
y = 3

shared_key = pow(g, x*y, p)
print('shared key is', shared_key)

c = 29

K_inv = pow(shared_key, -1, p)
M = (c * K_inv) % p
print('M =', M)
