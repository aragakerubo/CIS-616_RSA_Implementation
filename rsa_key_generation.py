#!/usr/bin/python3

# This file contains the code for generating the RSA keys.
# Steps to generate RSA keys:
# 1. Choose two distinct prime numbers, p and q.
# 2. Calculate n = p * q (modulus). The length of n in bits is the key length.
# 3. Calculate φ(n) = (p-1) * (q-1) (Euler's totient function).
# 4. Choose an integer e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1; e will be the public exponent.
# 5. Calculate d such that d * e ≡ 1 (mod φ(n)); d will be the private exponent.
# 6. The public key is (n, e) and the private key is (n, d).
# It is standard practice to convert the keys to PEM format for storage and exchange.

import random
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


# Function to generate a prime number
def generate_prime(bits):
    """
    Generate a prime number.
    Args:
        bits (int): The number of bits of the prime number.
    Returns:
        int: The prime number.
    """
    while True:
        num = random.getrandbits(bits)
        if is_prime(num):
            return num


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


# Function to calculate the modular inverse
def modinv(a, m):
    """
    Calculate the modular inverse of a number.
    Args:
        a (int): The number.
        m (int): The modulus.
    Returns:
        int: The modular inverse.
    """
    return pow(a, -1, m)


# Function to generate the RSA keys
def generate_rsa_keys(bits):
    """
    Generate the RSA keys.
    Args:
        bits (int): The number of bits of the RSA keys.
    Returns:
        tuple: The RSA keys (public key, private key).
    """
    p = generate_prime(bits // 2)
    q = generate_prime(bits // 2)
    while p == q:
        q = generate_prime(bits // 2)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    # e = 65537
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = modinv(e, phi)

    print("p:", p)
    print("q:", q)
    print("n:", n)
    print("phi:", phi)
    print("e:", e)
    print("d:", d)

    return (n, e), (n, d)


def pem_encode_rsa(modulus, exponent, tag):
    """
    Encode an RSA public or private key in PEM format.
    Args:
        modulus (int): The modulus of the key.
        exponent (int): The exponent of the key.
        tag (str): The tag of the key.
    Returns:
        str: The PEM-encoded key.
    """
    # Encode the modulus and exponent
    modulus_bytes = modulus.to_bytes((modulus.bit_length() + 7) // 8, "big")
    exponent_bytes = exponent.to_bytes((exponent.bit_length() + 7) // 8, "big")

    # Encode the modulus and exponent in base64
    modulus_b64 = base64.b64encode(modulus_bytes).decode()
    exponent_b64 = base64.b64encode(exponent_bytes).decode()

    # Create the PEM-encoded key
    pem = f"-----BEGIN {tag} KEY-----\n"
    pem += f"{modulus_b64}\n"
    pem += f"{exponent_b64}\n"
    pem += f"-----END {tag} KEY-----"

    return pem


# Main function
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rsa_key_generation.py <bits>")
        sys.exit(1)
    bits = int(sys.argv[1])
    public_key, private_key = generate_rsa_keys(bits)
    print("Public key (n, e):", public_key)
    print("Private key (n, d):", private_key)

    pem_encoded_public_key = pem_encode_rsa(
        public_key[0], public_key[1], "PUBLIC"
    )
    pem_encoded_private_key = pem_encode_rsa(
        private_key[0], private_key[1], "PRIVATE"
    )

    with open("public_key.pem", "w") as f:
        f.write(pem_encoded_public_key)

    with open("private_key.pem", "w") as f:
        f.write(pem_encoded_private_key)

    print("Keys saved in public_key.pem and private_key.pem.")
