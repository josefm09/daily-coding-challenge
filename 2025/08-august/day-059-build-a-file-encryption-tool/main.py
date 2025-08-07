#!/usr/bin/env python3
"""
Day 59: Build a file encryption tool
Date: August 07, 2025

365 Days of Code Challenge
"""

import os
from cryptography.fernet import Fernet, InvalidToken

# Get the directory where the script is located to robustly find the key file
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
KEY_PATH = os.path.join(SCRIPT_DIR, "secret.key")

def generate_key():
    """
    Generates a key and saves it into a file in the script's directory
    """
    key = Fernet.generate_key()
    with open(KEY_PATH, "wb") as key_file:
        key_file.write(key)
    print(f"✅ Key generated and saved to '{KEY_PATH}'")

def load_key():
    """
    Loads the key from the script's directory named `secret.key`
    """
    return open(KEY_PATH, "rb").read()

def encrypt_file(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and writes it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)
    print(f"✅ File '{filename}' encrypted successfully.")

def decrypt_file(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and writes it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()

    try:
        decrypted_data = f.decrypt(encrypted_data)
    except InvalidToken:
        print(f"❌ Error: Invalid key or corrupted data.")
        return

    with open(filename, "wb") as file:
        file.write(decrypted_data)
    print(f"✅ File '{filename}' decrypted successfully.")


import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple file encryption tool.")

    parser.add_argument("action", choices=["generate-key", "encrypt", "decrypt"],
                        help="Action to perform: generate-key, encrypt, or decrypt")
    parser.add_argument("-f", "--file", dest="filepath",
                        help="Path to the file to encrypt or decrypt")

    args = parser.parse_args()

    action = args.action
    filepath = args.filepath

    if action == "generate-key":
        generate_key()
    elif action in ["encrypt", "decrypt"]:
        if not filepath:
            parser.error(f"Action '{action}' requires a file. Use --file <path>.")
        if not os.path.exists(filepath):
            print(f"❌ Error: File not found at '{filepath}'")
            return

        try:
            key = load_key()
        except FileNotFoundError:
            print("❌ Error: 'secret.key' not found. Please generate a key first with 'generate-key'.")
            return

        if action == "encrypt":
            encrypt_file(filepath, key)
        elif action == "decrypt":
            decrypt_file(filepath, key)

if __name__ == "__main__":
    main()
