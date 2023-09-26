from cryptography.fernet import Fernet
import os


__key_file_path = 'ressources/secret.key'


def init() -> Fernet:
    if not os.path.isfile(__key_file_path):
        __create_key_file()    

    with open(__key_file_path, 'rb') as key_file:
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
    with open(__key_file_path, 'wb') as key_file:
        key_file.write(key)


def __create_key_file() -> None:
    f = open(__key_file_path, "wb")
    f.close()
