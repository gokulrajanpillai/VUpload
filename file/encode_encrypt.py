import argparse
import base64
from cryptography.fernet import Fernet

def encode_file(input_file, output_file):
    with open(input_file, 'rb') as infile:
        data = infile.read()
        encoded_data = base64.b64encode(data)
    
    with open(output_file, 'wb') as outfile:
        outfile.write(encoded_data)

def encrypt_file(input_file, output_file, encryption_key):
    with open(input_file, 'rb') as infile:
        data = infile.read()
    
    cipher_suite = Fernet(encryption_key)
    encrypted_data = cipher_suite.encrypt(data)
    
    with open(output_file, 'wb') as outfile:
        outfile.write(encrypted_data)

def main():
    parser = argparse.ArgumentParser(description="Encode and encrypt a file with user-defined parameters.")
    parser.add_argument("input_file", help="Input file to process")
    parser.add_argument("output_file", help="Output file to save the result")
    parser.add_argument("--encode", action="store_true", help="Encode the input file")
    parser.add_argument("--encrypt", action="store_true", help="Encrypt the input file")
    parser.add_argument("--encryption_key", help="Encryption key (required for encryption)")

    args = parser.parse_args()

    if args.encode:
        encode_file(args.input_file, args.output_file)
        print(f"File encoded and saved to {args.output_file}")
    elif args.encrypt:
        if not args.encryption_key:
            print("Encryption key is required for encryption.")
            return
        encryption_key = args.encryption_key.encode()
        encrypt_file(args.input_file, args.output_file, encryption_key)
        print(f"File encrypted and saved to {args.output_file}")

if __name__ == "__main__":
    main()
