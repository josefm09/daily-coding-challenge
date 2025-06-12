#!/usr/bin/env python3
"""
Test script for the file encryption tool
"""

import os
import tempfile
from file_encryptor import FileEncryptor

def test_encryption_decryption():
    """Test basic encryption and decryption functionality."""
    encryptor = FileEncryptor()
    test_password = "test_password_123"
    test_content = b"This is a test file with some binary data: \x00\x01\x02\x03"
    
    # Create temporary files
    with tempfile.NamedTemporaryFile(delete=False) as original_file:
        original_file.write(test_content)
        original_path = original_file.name
    
    encrypted_path = original_path + ".encrypted"
    decrypted_path = original_path + ".decrypted"
    
    try:
        # Test encryption
        print("Testing encryption...")
        success = encryptor.encrypt_file(original_path, encrypted_path, test_password)
        assert success, "Encryption failed"
        assert os.path.exists(encrypted_path), "Encrypted file not created"
        
        # Test decryption
        print("Testing decryption...")
        encryptor = FileEncryptor()  # New instance
        success = encryptor.decrypt_file(encrypted_path, decrypted_path, test_password)
        assert success, "Decryption failed"
        assert os.path.exists(decrypted_path), "Decrypted file not created"
        
        # Verify content matches
        with open(decrypted_path, 'rb') as f:
            decrypted_content = f.read()
        
        assert decrypted_content == test_content, "Decrypted content doesn't match original"
        
        print("✅ All tests passed!")
        
    finally:
        # Cleanup
        for path in [original_path, encrypted_path, decrypted_path]:
            if os.path.exists(path):
                os.unlink(path)

def test_wrong_password():
    """Test that wrong password fails decryption."""
    encryptor = FileEncryptor()
    test_content = b"Secret content"
    correct_password = "correct_password"
    wrong_password = "wrong_password"
    
    with tempfile.NamedTemporaryFile(delete=False) as original_file:
        original_file.write(test_content)
        original_path = original_file.name
    
    encrypted_path = original_path + ".encrypted"
    decrypted_path = original_path + ".decrypted"
    
    try:
        # Encrypt with correct password
        encryptor.encrypt_file(original_path, encrypted_path, correct_password)
        
        # Try to decrypt with wrong password
        print("Testing wrong password...")
        encryptor = FileEncryptor()
        success = encryptor.decrypt_file(encrypted_path, decrypted_path, wrong_password)
        assert not success, "Decryption should have failed with wrong password"
        
        print("✅ Wrong password test passed!")
        
    finally:
        # Cleanup
        for path in [original_path, encrypted_path, decrypted_path]:
            if os.path.exists(path):
                os.unlink(path)

if __name__ == "__main__":
    print("Running encryption tool tests...")
    test_encryption_decryption()
    test_wrong_password()
    print("\n✨ All tests completed successfully!")

