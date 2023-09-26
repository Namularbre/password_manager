from utils.password_generator import generate_password
from utils.security import encrypt, decrypt
from entity.password import Password 
import os


class PasswordModel:
    def __init__(self) -> None:
        self.path = "./ressources/pass.csv"
        self.passwords = []
        if not os.path.isfile(self.path):
            self.__create_pass_file()
        self.__load()

    def create_password(self, site) -> None:
        password = generate_password()
        encrypted_password = encrypt(password)
        self.passwords.append(Password(site, encrypted_password))
        self.__save()

    def get_sites(self) -> list:
        sites = []
        for password in self.passwords:
            sites.append(password.site)
        return sites
    
    def get_password(self, site) -> str|None:
        for password in self.passwords:
            if password.site == site:
                return decrypt(password.value)
        return None
    
    def site_exists(self, site) -> bool:
        for password in self.passwords:
            if password.site == site:
                return True
        return False
    
    def __create_pass_file(self) -> None:
        f = open(self.path, 'w')
        f.close()
    
    def __load(self) -> None:
        file = open(self.path, "r")
        for raw_line in file.readlines():
            line = raw_line.split(',')
            self.passwords.append(Password(line[0], line[1]))
        file.close()

    def __save(self) -> None:
        file = open(self.path, "w")
        str_passwords = ""
        for password in self.passwords:
            str_passwords += str(password)
        file.write(str_passwords)
        file.close()
