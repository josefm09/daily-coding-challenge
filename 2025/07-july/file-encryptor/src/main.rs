use file_encryptor::Encryptor;
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() != 4 {
        eprintln!("Usage: {} <encrypt|decrypt> <input_file> <output_file>", args[0]);
        std::process::exit(1);
    }

    let command = &args[1];
    let input_file = &args[2];
    let output_file = &args[3];

    // Use a fixed key for demonstration (in production, use proper key management)
    let key = [1u8; 32];
    let encryptor = Encryptor::new(&key);

    let result = match command.as_str() {
        "encrypt" => encryptor.encrypt_file(input_file, output_file),
        "decrypt" => encryptor.decrypt_file(input_file, output_file),
        _ => {
            eprintln!("Invalid command. Use 'encrypt' or 'decrypt'");
            std::process::exit(1);
        }
    };

    if let Err(e) = result {
        eprintln!("Error: {}", e);
        std::process::exit(1);
    }
}