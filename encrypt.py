# import required module
from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)

with open('name.csv', 'rb') as file:
    original = file.read()
    
fernet = Fernet(key)
    
encrypted = fernet.encrypt(data = original)

with open('name.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)