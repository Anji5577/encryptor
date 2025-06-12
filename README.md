
# 🔐 File Encryptor (Terminal-Based)

A simple and secure terminal-based Python script to **encrypt and decrypt files** using a password. Built using the `cryptography` library with AES-level security (Fernet).

---------------------------------------------------------------------------------------------------------------------------------------------

## ✅ Features

- 🔒 Secure file encryption with password
- 🔓 Decrypt with the same password
- 📂 Works with any file type (text, PDF, images, etc.)
- 🚫 Prevents access without correct password
- 🧠 Simple command-line usage

---------------------------------------------------------------------------------------------------------------------------------------------
# for windows 
Requirements
- Python 3.x
- `cryptography` library
# Install Requirements
pip install cryptography
# for macOs
Requirements

- Python 3.x
- `cryptography` library
#Install Requirements
  
brew install cryptography
---------------------------------------------------------------------------------------------------------------------------------------------
#usage

python3 encryptor.py encrypt <file_path> <password>

python3 encryptor.py decrypt <file_path.enc> <password>

