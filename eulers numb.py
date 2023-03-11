def fact(n):
    f = 1
    for i in range(2, n+1):
        f *= i
    return f

def e(prec):
    aprox = 0
    for n in range(prec):
        aprox += 1 / fact(n)
    return aprox

print(e(121))      # 2.718282
print(e(100))      # 2.718282
print(e(1000))      # 2.718282