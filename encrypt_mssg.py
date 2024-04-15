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
import base64


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


# Main function
if __name__ == "__main__":
    # Check
    if not len(sys.argv) > 1:
        print("Usage: python encrypt_mssg.py <message>")
        sys.exit(1)

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

    # The message to encrypt
    message = " ".join(sys.argv[1:])

    # Convert the message to an integer list
    m = [string_to_int(message_char) for message_char in message]

    # Encrypt the message
    c = [encrypt(message_char, e, n) for message_char in m]

    # Convert the encrypted message to a base64 string
    c = str(c)
    print("Encrypted message before encoding:", c)
    encoded_c_b64 = base64.b64encode(c.encode()).decode()

    # Print the encrypted message
    print("Encrypted message after encoding:", encoded_c_b64)

    # Write the encrypted message to a file
    with open("encrypted_message.txt", "w") as file:
        file.write(encoded_c_b64)
        file.write("\n")
