# data-encryption-and-decryption-with-fernet

## Project Overview
This repository contains a Python implementation demonstrating symmetric data encryption and decryption using the Fernet algorithm from the Python `cryptography` library. It provides a simple example of key generation, file encryption, and file decryption (specifically targeting CSV files).

## Tech Stack
- **Programming Language**: Python 3
- **Libraries**: `cryptography` (specifically `cryptography.fernet`)

## Key Implementation Details
- **Symmetric Key Generation**: Generates a secure symmetric key using `Fernet.generate_key()` and saves it locally to `key.key`.
- **Encryption Process**: Loads the symmetric key, instantiates a `Fernet` cipher suite, reads a target file (e.g. `data.csv`), encrypts the bytes, and writes the encrypted payload to a new file (e.g. `encryptdata.csv`).
- **Decryption Process**: Reads the encrypted payload, decrypts it using the same symmetric key, and writes the original decrypted output to a new file (e.g. `decryptdata.csv`).
