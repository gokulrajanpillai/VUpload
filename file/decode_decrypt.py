import argparse
import base64
from cryptography.fernet import Fernet

def decode_file(input_file, output_file):
    with open(input_file, 'rb') as infile:
        encoded_data = infile.read()
        decoded_data = base64.b64decode(encoded_data)
    
    with open(output_file, 'wb') as outfile:
        outfile.write(decoded_data)

def decrypt_file(input_file, output_file, decryption_key):
    with open(input_file, 'rb') as infile:
        encrypted_data = infile.read()
    
    cipher_suite = Fernet(decryption_key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    
    with open(output_file, 'wb') as outfile:
        outfile.write(decrypted_data)

def main():
    parser = argparse.ArgumentParser(description="Decode and decrypt a file with user-defined parameters.")
    parser.add_argument("input_file", help="Input file to process")
    parser.add_argument("output_file", help="Output file to save the result")
    parser.add_argument("--decode", action="store_true", help="Decode the input file")
    parser.add_argument("--decrypt", action="store_true", help="Decrypt the input file")
    parser.add_argument("--decryption_key", help="Decryption key (required for decryption)")

    args = parser.parse_args()

    if args.decode:
        decode_file(args.input_file, args.output_file)
        print(f"File decoded and saved to {args.output_file}")
    elif args.decrypt:
        if not args.decryption_key:
            print("Decryption key is required for decryption.")
            return
        decryption_key = args.decryption_key.encode()
        decrypt_file(args.input_file, args.output_file, decryption_key)
        print(f"File decrypted and saved to {args.output_file}")

if __name__ == "__main__":
    main()
