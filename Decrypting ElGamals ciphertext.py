import math

def find_private_key(p, g, gx):
    """Find the private key x given the public key parameters p, g, and gx."""
    x = 1
    while pow(g, x, p) != gx:
        x += 1
    return x

def decrypt_message(p, gy, shared_key, c, x):
    """Decrypt the ciphertext c using the shared key and modulus p."""
    K_inv = pow(shared_key, p-1-x, p)  # calculate the modular inverse using pow()
    M = (c * K_inv) % p
    return M

# Prompt the user for the ElGamal parameters and the message to decrypt
p = int(input("Enter a value of p: "))
g = int(input("Enter a value of g: "))
gx = int(input("Enter a value of gx: "))
x = int(input("Enter a value of x: "))
gy = input("Enter a value of gy (in the format c.gy): ")

# Find the private key
x = find_private_key(p, g, gx)
print('Private key is', x)

# Decrypt the message
c, gy_val = map(int, gy.split('.'))
shared_key = pow(gy_val, x, p)
M = decrypt_message(p, gy_val, shared_key, c, x)
print('Decrypted message is', M)
