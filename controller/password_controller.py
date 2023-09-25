from model.password import PasswordModel

class PasswordController:
    def __init__(self) -> None:
        self.model = PasswordModel()

    def get_sites(self) -> list:
        return self.model.get_sites()

    def get_password(self, site) -> str:
        password = self.model.get_password(site)
        if password != None:
            return password
        else:
            return "Site inconnu"
        
    def create_password(self, site) -> None:
        if not self.model.site_exists(site):
            self.model.create_password(site)

    def search_site(self, search) -> list:
        sites = self.get_sites()
        result = []
        for site in sites:
            if search.lower() in site.lover():
                result.append(site)
        return result
