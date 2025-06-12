import sys
from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(password: str) -> bytes:
    # Derive a Fernet key from the password using SHA-256
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)

def encrypt_file(file_path, password):
    key = generate_key(password)
    fernet = Fernet(key)

    try:
        with open(file_path, 'rb') as f:
            data = f.read()
    except FileNotFoundError:
        print("❌ File not found.")
        return

    encrypted = fernet.encrypt(data)
    with open(file_path + '.enc', 'wb') as f:
        f.write(encrypted)

    print(f"✅ File encrypted: {file_path}.enc")

def decrypt_file(file_path, password):
    key = generate_key(password)
    fernet = Fernet(key)

    try:
        with open(file_path, 'rb') as f:
            encrypted = f.read()
    except FileNotFoundError:
        print("❌ File not found.")
        return

    try:
        decrypted = fernet.decrypt(encrypted)
    except Exception as e:
        print("❌ Decryption failed. Wrong password or file corrupted.")
        return

    out_file = file_path.replace('.enc', '.dec')
    with open(out_file, 'wb') as f:
        f.write(decrypted)

    print(f"✅ File decrypted: {out_file}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python file_encryptor.py [encrypt|decrypt] <file_path> <password>")
        return

    action, file_path, password = sys.argv[1], sys.argv[2], sys.argv[3]

    if action == 'encrypt':
        encrypt_file(file_path, password)
    elif action == 'decrypt':
        decrypt_file(file_path, password)
    else:
        print("❌ Invalid action. Use 'encrypt' or 'decrypt'.")

if __name__ == '__main__':
    main()

