#!/usr/bin/python3

# This file contains the code for cracking the RSA keys.
# Steps to crack RSA keys:
# 1. Factorize n to get p and q.
# 2. Calculate φ(n) = (p-1) * (q-1) (Euler's totient function).
# 3. Choose an integer e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1;
#    e will be the public exponent.
# 4. Calculate d such that d * e ≡ 1 (mod φ(n));
#    d will be the private exponent.
# 5. The public key is (n, e) and the private key is (n, d).

import math
import base64
import sys


# Function to check if a number is prime
def is_prime(num):
    """
    Check if a number is prime.
    Args:
        num (int): The number to check.
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


# Function to calculate the greatest common divisor
def gcd(a, b):
    """
    Calculate the greatest common divisor of two numbers.
    Args:
        a (int): The first number.
        b (int): The second number.
    Returns:
        int: The greatest common divisor.
    """
    while b != 0:
        a, b = b, a % b
    return a


# Function to factorize n
def factorize(n):
    """
    Factorize n into two prime numbers.
    Args:
        n (int): The number to factorize.
    Returns:
        tuple: The two prime factors.
    """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    return None, None


# Function to calculate the modular inverse
def modinv(a, m):
    """
    Calculate the modular inverse of a modulo m.
    Args:
        a (int): The number.
        m (int): The modulo.
    Returns:
        int: The modular inverse.
    """
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1


# Function to crack the RSA keys
def crack_rsa(n, e):
    """
    Crack the RSA keys.
    Args:
        n (int): The modulus.
        e (int): The public exponent.
    Returns:
        tuple: The private exponent and the prime factors of n.
    """
    # Factorize n
    p, q = factorize(n)
    if p is None or q is None:
        print("Failed to factorize n.")
        sys.exit(1)

    # Calculate φ(n)
    phi = (p - 1) * (q - 1)

    # Calculate the private exponent
    d = modinv(e, phi)

    return phi, d, p, q


# Main function
if __name__ == "__main__":
    # The public key (n, e)
    # Read the public key from the file
    with open("public_key.pem", "r") as file:
        public_key = file.read().splitlines()

        # Get the modulus and the public exponent
        n = public_key[1]
        e = public_key[2]

        # Decode the base64 strings
        n = base64.b64decode(n)
        e = base64.b64decode(e)

        # Convert bytes to integers
        n = int.from_bytes(n, byteorder="big")
        e = int.from_bytes(e, byteorder="big")

    # Crack the RSA keys
    phi, d, p, q = crack_rsa(n, e)
    print("Cracked private key:")
    print("phi:", phi)
    print("p:", p)
    print("q:", q)
    print("d:", d)

    # Write the private key to the file
    with open("cracked_private_key.pem", "w") as file:
        # Encode the modulus and exponent
        modulus_bytes = n.to_bytes((n.bit_length() + 7) // 8, "big")
        exponent_bytes = d.to_bytes((d.bit_length() + 7) // 8, "big")

        # Encode the modulus and exponent in base64
        modulus_b64 = base64.b64encode(modulus_bytes).decode()
        exponent_b64 = base64.b64encode(exponent_bytes).decode()

        # Write the encoded key to the file
        file.write("-----BEGIN PRIVATE KEY-----\n")
        file.write(f"{modulus_b64}\n")
        file.write(f"{exponent_b64}\n")
        file.write("-----END PRIVATE KEY-----")

    print("Private key written to cracked_private_key.txt.")
    print("Done.")
