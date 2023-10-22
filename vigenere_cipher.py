import argparse
import os

def encrypt_vigenere(plain_text, key):
    encrypted_text = ""
    key_length = len(key)
    key_index = 0
    for char in plain_text:
        if char.isalpha():
            key_shift = ord(key[key_index % key_length].upper()) - 65
            if char.isupper():
                encrypted_text += chr((ord(char) - 65 + key_shift) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) - 97 + key_shift) % 26 + 97)
            key_index += 1
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_vigenere(encrypted_text, key):
    decrypted_text = ""
    key_length = len(key)
    key_index = 0
    for char in encrypted_text:
        if char.isalpha():
            key_shift = ord(key[key_index % key_length].upper()) - 65
            if char.isupper():
                decrypted_text += chr((ord(char) - 65 - key_shift) % 26 + 65)
            else:
                decrypted_text += chr((ord(char) - 97 - key_shift) % 26 + 97)
            key_index += 1
        else:
            decrypted_text += char
    return decrypted_text

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Vigenère Cipher Encryption and Decryption of a Text File')
    parser.add_argument('input_file', help='Path to the input file')
    parser.add_argument('--output_file', help='Path to the output file', default="")
    parser.add_argument('--key', help='Encryption/Decryption key', default='secret')
    parser.add_argument('--decrypt', action='store_true', help='Flag to decrypt the text')

    args = parser.parse_args()

    if not args.output_file:
        input_file_name, _ = os.path.splitext(args.input_file)
        if args.decrypt:
            args.output_file = f"decrypted_{os.path.basename(input_file_name)}.txt"
        else:
            args.output_file = f"encrypted_{os.path.basename(input_file_name)}.txt"

    try:
        with open(args.input_file, 'r') as file:
            input_text = file.read()
            if args.decrypt:
                output_text = decrypt_vigenere(input_text, args.key)
            else:
                output_text = encrypt_vigenere(input_text, args.key)

            with open(args.output_file, 'w') as output_file:
                output_file.write(output_text)

            if args.decrypt:
                print(f"Decryption successful. Decrypted text written to {args.output_file}")
            else:
                print(f"Encryption successful. Encrypted text written to {args.output_file}")
    except FileNotFoundError:
        print("Input file not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")
