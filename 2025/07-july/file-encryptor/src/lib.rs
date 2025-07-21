use aes_gcm::{Aes256Gcm, Key, Nonce};
use aes_gcm::aead::Aead;
use aes_gcm::KeyInit;
use rand::{Rng, thread_rng};
use std::fs;
use base64::{Engine as _, engine::general_purpose};

pub struct Encryptor {
    cipher: Aes256Gcm,
}

impl Encryptor {
    pub fn new(key: &[u8; 32]) -> Self {
        let cipher_key = Key::<Aes256Gcm>::from_slice(key);
        let cipher = Aes256Gcm::new(cipher_key);
        Self { cipher }
    }

    pub fn encrypt_file(&self, input_path: &str, output_path: &str) -> Result<(), Box<dyn std::error::Error>> {
        let data = fs::read(input_path)?;
        
        // Generate a random 12-byte nonce
        let mut rng = thread_rng();
        let mut nonce_bytes = [0u8; 12];
        rng.fill(&mut nonce_bytes);
        let nonce = Nonce::from_slice(&nonce_bytes);

        // Encrypt the data
        let encrypted_data = self.cipher.encrypt(nonce, data.as_ref())
            .map_err(|_| "Encryption failed")?;

        // Combine nonce and encrypted data
        let mut final_data = nonce.to_vec();
        final_data.extend(encrypted_data);

        // Base64 encode the result
        let encoded = general_purpose::STANDARD.encode(final_data);
        
        fs::write(output_path, encoded)?;
        Ok(())
    }

    pub fn decrypt_file(&self, input_path: &str, output_path: &str) -> Result<(), Box<dyn std::error::Error>> {
        let encoded_data = fs::read_to_string(input_path)?;
        let data = general_purpose::STANDARD.decode(encoded_data)?;

        // Split nonce and encrypted data
        let nonce = Nonce::from_slice(&data[..12]);
        let encrypted_data = &data[12..];

        // Decrypt the data
        let decrypted_data = self.cipher.decrypt(nonce, encrypted_data.as_ref())
            .map_err(|_| "Decryption failed")?;

        fs::write(output_path, decrypted_data)?;
        Ok(())
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use tempfile::NamedTempFile;
    use std::io::Write;

    #[test]
    fn test_encryption_decryption() {
        let key = [1u8; 32];
        let encryptor = Encryptor::new(&key);

        // Create a temporary file with test data
        let mut input_file = NamedTempFile::new().unwrap();
        let test_data = b"Hello, World!";
        input_file.write_all(test_data).unwrap();

        // Create temporary files for encrypted and decrypted data
        let encrypted_file = NamedTempFile::new().unwrap();
        let decrypted_file = NamedTempFile::new().unwrap();

        // Test encryption and decryption
        encryptor.encrypt_file(
            input_file.path().to_str().unwrap(),
            encrypted_file.path().to_str().unwrap()
        ).unwrap();

        encryptor.decrypt_file(
            encrypted_file.path().to_str().unwrap(),
            decrypted_file.path().to_str().unwrap()
        ).unwrap();

        let decrypted_content = fs::read(decrypted_file.path()).unwrap();
        assert_eq!(decrypted_content, test_data);
    }
}
