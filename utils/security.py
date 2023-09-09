from cryptography.fernet import Fernet

def init() -> Fernet:
    with open('ressources/secret.key', 'rb') as key_file:
        key = key_file.read()

    if not key:
        key = Fernet.generate_key()
        __save_key(key)
    return Fernet(key)

def encrypt(plain_text) -> bytes:
    cipher_suite = init()
    encrypted_text = cipher_suite.encrypt(plain_text.encode())
    return encrypted_text

def decrypt(encrypted_text) -> str:
    cipher_suite = init()
    decrypted_text = cipher_suite.decrypt(encrypted_text)
    return decrypted_text.decode()

def __save_key(key) -> None:
    with open('ressources/secret.key', 'wb') as key_file:
        key_file.write(key)
