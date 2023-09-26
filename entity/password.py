class Password:
    def __init__(self, site, value) -> None:
        self.site = site
        self.value = value

    def __str__(self) -> str:
        return self.site + "," + str(self.value) + ",\n"
