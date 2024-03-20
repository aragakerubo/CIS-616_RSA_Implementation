# RSA Algorithm Implementation

## RSA Algorithm Basics:

The RSA algorithm is a widely used asymmetric cryptographic algorithm invented by Ron Rivest, Adi Shamir, and Leonard Adleman in 1977. It is based on the mathematical properties of large prime numbers.

## Key Components:

1. **Public Key:** Used for encryption. It is derived from the product of two large prime numbers and a public exponent.
2. **Private Key:** Used for decryption. It is derived from the same two large prime numbers and a private exponent.
3. **Modulus:** The product of the two large prime numbers used in key generation. It is part of both the public and private keys.

## Process of key generation, encryption, and decryption

### 1. Key Generation:

1. Choose two distinct prime numbers, p and q.
2. Calculate n = p \* q (modulus). The length of n in bits is the key length.
3. Calculate φ(n) = (p-1) \* (q-1) (Euler's totient function).
4. Choose an integer e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1; e will be the public exponent.
5. Calculate d such that d \* e ≡ 1 (mod φ(n)); d will be the private exponent.
6. The public key is (n, e) and the private key is (n, d).

### 2. Encryption:

1. Convert the message to an integer.
2. Compute the ciphertext c = m^e (mod n). Note: The message m must be less than n.
3. The ciphertext c is the encrypted message.

### 3. Decryption:

1. Compute the plaintext message m = c^d (mod n).

## Cracking RSA encryption

Cracking RSA encryption is a complex and computationally intensive task, especially for RSA keys with large key sizes.
Here are the general steps involved in attempting to crack RSA encryption:

1. Factorize n to get p and q.
2. Calculate φ(n) = (p-1) \* (q-1) (Euler's totient function).
3. Choose an integer e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1; e will be the public exponent.
4. Calculate d such that d \* e ≡ 1 (mod φ(n)); d will be the private exponent.
5. The public key is (n, e) and the private key is (n, d).

## Real-World Applications:

-   Secure communication over the internet (e.g., HTTPS, SSH)
-   Digital signatures for authentication and non-repudiation
-   Secure email communication (e.g., PGP)

## Benefits of RSA:

-   Strong security based on the difficulty of factoring large numbers
-   Supports secure key exchange without the need for a pre-shared secret
-   Enables digital signatures for authentication and integrity verification

## Key Length and Security:

-   Longer key lengths (e.g., 2048 bits or higher) offer higher security against brute-force attacks.
-   Shorter key lengths are less secure and vulnerable to attacks.
-   Best Practices for Key Management:

## Use strong, randomly generated prime numbers for key generation.

-   Store private keys securely and use them only when necessary.
-   Regularly update keys and algorithms to ensure security against evolving threats.

## Instructions

### Requirements

-   Python 3.x

### Usage

1. Clone the repository:

```bash
git clone https://github.com/aragakerubo/CIS-616_RSA_Implementation.git
```

2. Navigate to the project directory:

```bash
cd CIS-616_RSA_Implementation
```

3. Run the script with the desired key size (in bits):

```bash
python rsa_key_generation.py 256
```

4. Replace 256 with the desired key size (e.g., 256, 512, 1024, 2048).

5. The script will generate RSA keys and save them to public_key.txt and private_key.txt. It will also encrypt and decrypt a sample message.

## Files

-   `rsa_key_generation.py`: The main Python script that generates RSA keys, encrypts, and decrypts messages.
-   `encrypt_mssg.py`: Python script to encrypt a message using the public key.
-   `decrypt_mssg.py`: Python script to decrypt a message using the private key.
-   `crack_rsa.py`: Python script to crack RSA encryption by factorizing the modulus.
-   `public_key.txt`: The file where the public key (n, e) is saved.
-   `private_key.txt`: The file where the private key (n, d) is saved.
-   `cracked_private_key.txt`: The file where the cracked private key (n, e) is saved.

## Example

Here's an example of how to use the RSA implementation:

1. Run `crack_rsa.py` to generate RSA keys with a key size of 256 bits.

```bash
./crack_rsa.py 256
```

2. To encrypt a sample message with the newly generated public key, run `encrypt_mssg.py`.

```bash
./encrypt_mssg.py "Hello, World!"
```

3. To decrypt the encrypted message, run `decrypt_mssg.py`.

```bash
./decrypt_mssg.py
```

4. To attempt to crack RSA encryption by factorizing the modulus from the public key, run `crack_rsa.py`.

```bash
./crack_rsa.py
```

This command sequence will generate RSA keys with a key size of 256 bits, encrypt a message, decrypt the encrypted message, and attempt to crack RSA encryption.
