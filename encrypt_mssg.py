#!/usr/bin/python3

# This file contains the code for encrypting a message using the RSA algorithm.
# Steps to encrypt a message:
# 1. Convert the message to an integer.
# 2. Compute the ciphertext c = m^e (mod n),
#    where m is the plaintext message,
#    e is the public exponent, and n is the modulus.
#    Note: The message m must be less than n.
# 3. The ciphertext c is the encrypted message.

# Note: Be sure to choose a sufficiently large key size such that the message m is less than n.
# Assuming we have the message m in ASCII format, n must be greater than 255 (2^8) to encrypt a single character.

# Import the sys module
import sys


# Function to encrypt a message
def encrypt(m, e, n):
    """
    Encrypt a message using the RSA algorithm.
    Args:
        m (int): The plaintext message.
        e (int): The public exponent.
        n (int): The modulus.
    Returns:
        int: The encrypted message.
    """
    c = pow(m, e, n)
    return c


# Function to convert a string to an integer
def string_to_int(s):
    """
    Convert a string to an integer.
    Args:
        s (str): The string to convert.
    Returns:
        int: The integer.
    """
    return int.from_bytes(s.encode(), "big")


# Function to convert an integer to a string
def int_to_string(n):
    """
    Convert an integer to a string.
    Args:
        n (int): The integer to convert.
    Returns:
        str: The string.
    """
    return n.to_bytes((n.bit_length() + 7) // 8, "big").decode()


# Main function
if __name__ == "__main__":
    # The public key (n, e)
    # Read the public key from the file

    with open("public_key.txt", "r") as file:
        n = int(file.readline())
        e = int(file.readline())

    # The message to encrypt
    message = sys.argv[1]

    # Convert the message to an integer list
    m = [string_to_int(message_char) for message_char in message]

    # Encrypt the message
    c = [encrypt(message_char, e, n) for message_char in m]

    # Print the encrypted message
    print("Encrypted message:", c)

    # Write the encrypted message to a file
    with open("encrypted_message.txt", "w") as file:
        file.write(str(c))
        file.write("\n")
