#!/usr/bin/env python3
"""
Daily Coding Challenge - Day 002
File Encryption Tool

A simple command-line tool for encrypting and decrypting files using AES encryption.

Author: Jose
Date: June 12, 2025
"""

import os
import sys
import getpass
import argparse
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64


class FileEncryptor:
    """A simple file encryption/decryption tool using Fernet (AES 128)."""
    
    def __init__(self):
        self.key = None
        self.fernet = None
    
    def derive_key_from_password(self, password: str, salt: bytes) -> bytes:
        """Derive a key from password using PBKDF2."""
        password_bytes = password.encode('utf-8')
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password_bytes))
        return key
    
    def setup_encryption(self, password: str, salt: bytes = None) -> bytes:
        """Set up encryption with a password."""
        if salt is None:
            salt = os.urandom(16)
        
        self.key = self.derive_key_from_password(password, salt)
        self.fernet = Fernet(self.key)
        return salt
    
    def encrypt_file(self, input_file: str, output_file: str, password: str) -> bool:
        """Encrypt a file."""
        try:
            # Generate salt for key derivation
            salt = self.setup_encryption(password)
            
            # Read the original file
            with open(input_file, 'rb') as f:
                file_data = f.read()
            
            # Encrypt the data
            encrypted_data = self.fernet.encrypt(file_data)
            
            # Write salt + encrypted data to output file
            with open(output_file, 'wb') as f:
                f.write(salt + encrypted_data)
            
            print(f"✅ File encrypted successfully: {output_file}")
            return True
            
        except Exception as e:
            print(f"❌ Encryption failed: {str(e)}")
            return False
    
    def decrypt_file(self, input_file: str, output_file: str, password: str) -> bool:
        """Decrypt a file."""
        try:
            # Read the encrypted file
            with open(input_file, 'rb') as f:
                file_data = f.read()
            
            # Extract salt (first 16 bytes) and encrypted data
            salt = file_data[:16]
            encrypted_data = file_data[16:]
            
            # Setup decryption with the same salt
            self.setup_encryption(password, salt)
            
            # Decrypt the data
            decrypted_data = self.fernet.decrypt(encrypted_data)
            
            # Write decrypted data to output file
            with open(output_file, 'wb') as f:
                f.write(decrypted_data)
            
            print(f"✅ File decrypted successfully: {output_file}")
            return True
            
        except Exception as e:
            print(f"❌ Decryption failed: {str(e)}")
            return False


def main():
    parser = argparse.ArgumentParser(
        description="File Encryption Tool - Encrypt/Decrypt files with AES encryption"
    )
    parser.add_argument(
        'mode', 
        choices=['encrypt', 'decrypt'], 
        help='Operation mode: encrypt or decrypt'
    )
    parser.add_argument(
        'input_file', 
        help='Input file path'
    )
    parser.add_argument(
        'output_file', 
        help='Output file path'
    )
    parser.add_argument(
        '--password', 
        help='Encryption password (will prompt if not provided)'
    )
    
    args = parser.parse_args()
    
    # Validate input file exists
    if not os.path.exists(args.input_file):
        print(f"❌ Input file not found: {args.input_file}")
        sys.exit(1)
    
    # Get password
    if args.password:
        password = args.password
    else:
        password = getpass.getpass("Enter password: ")
    
    if not password:
        print("❌ Password cannot be empty")
        sys.exit(1)
    
    # Create encryptor instance
    encryptor = FileEncryptor()
    
    # Perform operation
    if args.mode == 'encrypt':
        success = encryptor.encrypt_file(args.input_file, args.output_file, password)
    else:
        success = encryptor.decrypt_file(args.input_file, args.output_file, password)
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

