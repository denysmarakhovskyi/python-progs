def encrypt_rsa():
    # Get user input for Z, n, and e
    Z = int(input("Enter the message you want to encrypt (Z): "))
    n = int(input("Enter the modulus (n - start value): "))
    e = int(input("Enter the public exponent (e - end value): "))
    
    # Calculate the encrypted message
    encrypted = pow(Z, e, n)
    
    # Print the encrypted message
    print("Encrypted message: {}".format(encrypted))

encrypt_rsa()