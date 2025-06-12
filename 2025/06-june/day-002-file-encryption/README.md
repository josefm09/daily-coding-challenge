# Day 002 - File Encryption Tool

**Date:** June 12, 2025  
**Difficulty:** Intermediate  
**Estimated Time:** 1-2 hours

## Challenge Description

Build a command-line file encryption tool that can securely encrypt and decrypt files using AES encryption.

## Features Implemented

- ✅ AES encryption using Fernet (symmetric encryption)
- ✅ Password-based key derivation using PBKDF2
- ✅ Salt generation for security
- ✅ Command-line interface
- ✅ Error handling and validation
- ✅ Support for any file type (binary safe)

## Requirements

```bash
pip install cryptography
```

## Usage

### Encrypting a file
```bash
python3 file_encryptor.py encrypt input.txt encrypted.bin
```

### Decrypting a file
```bash
python3 file_encryptor.py decrypt encrypted.bin decrypted.txt
```

### Using password as argument (not recommended for production)
```bash
python3 file_encryptor.py encrypt input.txt encrypted.bin --password mypassword
```

## Security Features

1. **PBKDF2 Key Derivation**: Uses 100,000 iterations with SHA-256
2. **Salt**: Random 16-byte salt for each encryption
3. **AES Encryption**: Fernet provides AES 128 in CBC mode with HMAC
4. **Password Protection**: Prompts for password securely (hidden input)

## Example Test

```bash
# Create a test file
echo "This is a secret message!" > test.txt

# Encrypt it
python3 file_encryptor.py encrypt test.txt encrypted.bin

# Decrypt it
python3 file_encryptor.py decrypt encrypted.bin decrypted.txt

# Verify contents match
diff test.txt decrypted.txt
```

## What I Learned

- How to use the `cryptography` library for secure encryption
- PBKDF2 key derivation from passwords
- Importance of salts in cryptography
- Binary file handling in Python
- Command-line argument parsing with `argparse`
- Secure password input with `getpass`

## Possible Improvements

- Add support for multiple files
- Implement asymmetric encryption (RSA)
- Add file integrity verification
- GUI interface
- Progress bars for large files
- Compression before encryption

