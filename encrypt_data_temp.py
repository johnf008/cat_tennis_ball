from cryptography.fernet import Fernet

with open('file_key.key', "rb") as filekey:
    key = filekey.read()

fernet = Fernet(key)

with open("save_data/score.txt", "rb") as file:
    og = file.read()

encrypted = fernet.encrypt(og)

with open ("save_data/score.txt", "wb") as encrypted_file:
    encrypted_file.write(encrypted)