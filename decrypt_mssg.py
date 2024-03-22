#!/usr/bin/python3

# This file contains the code for decrypting a message using the RSA algorithm.
# Steps to decrypt a message:
# 1. Compute the plaintext message m = c^d (mod n),
#    where c is the encrypted message,
#    d is the private exponent, and n is the modulus.
# 2. Convert the integer m to a string.
# 3. The string is the decrypted message.


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
    # The private key (n, d)
    # Read the private key from the file
    with open("private_key.txt", "r") as file:
        n = int(file.readline())
        d = int(file.readline())

    # The encrypted message
    with open("encrypted_message.txt", "r") as file:
        c = [int(x) for x in file.readline()[1:-2].split(", ")]

    # Decrypt the message
    message = [decrypt(c[i], d, n) for i in range(len(c))]
    message = "".join(message)

    print("Decrypted message:", message)

    with open("decrypted_message.txt", "w") as file:
        file.write(message)
        file.write("\n")
