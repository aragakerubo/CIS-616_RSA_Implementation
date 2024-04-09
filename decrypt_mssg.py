#!/usr/bin/python3

# This file contains the code for decrypting a message using the RSA algorithm.
# Steps to decrypt a message:
# 1. Compute the plaintext message m = c^d (mod n),
#    where c is the encrypted message,
#    d is the private exponent, and n is the modulus.
# 2. Convert the integer m to a string.
# 3. The string is the decrypted message.

import base64


# Function to decrypt a message
def decrypt(c, d, n):
    """
    Decrypt a message using the RSA algorithm.
    Args:
        c (int): The encrypted message.
        d (int): The private exponent.
        n (int): The modulus.
    Returns:
        str: The decrypted message.
    """
    m = pow(c, d, n)
    return int_to_string(m)


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
    # The private key (n, d)
    # Read the private key from the file
    with open("private_key.pem", "r") as file:
        public_key = file.read().splitlines()

        # Get the modulus and the private exponent
        n = public_key[1]
        d = public_key[2]

        # Decode the base64 strings
        n = base64.b64decode(n)
        d = base64.b64decode(d)

        # Convert bytes to integers
        n = int.from_bytes(n, byteorder="big")
        d = int.from_bytes(d, byteorder="big")

    # The encrypted message
    with open("encrypted_message.txt", "r") as file:
        encoded_c_b64 = file.readline().strip()

    # Decode the base64 string
    c = list(
        map(int, base64.b64decode(encoded_c_b64).decode()[1:-1].split(", "))
    )
    print("Encrypted message:", c)

    # Decrypt the message
    message = [decrypt(c[i], d, n) for i in range(len(c))]
    message = "".join(message)

    print("Decrypted message:", message)

    with open("decrypted_message.txt", "w") as file:
        file.write(message)
        file.write("\n")
