# function to generate prime factors of a number
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# function to calculate modular inverse using extended Euclidean algorithm
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise ValueError('modular inverse does not exist')
    return x % m

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# prompt the user for the modulus n and calculate phi(n)
n = int(input("Enter the value of n (start numb): "))
factors = prime_factors(n)
phi_n = 1
for factor in set(factors):
    phi_n *= factor - 1

# prompt the user for the encryption exponent e and calculate the decryption exponent d
e = int(input("Enter the encryption exponent (e - end number): "))
d = modinv(e, phi_n)
print("The decryption exponent (d) is:", d)

# prompt the user for the ciphertext Z, and decrypt the message
Z = int(input("Enter the ciphertext (Z): "))
M = pow(Z, d, n)
print("The decrypted message M is:", M)
