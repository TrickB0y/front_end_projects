class Autor:
    def __init__(
            self,
            nome = "",
            foto = "",
            bio = "",
            obras = []
        ):
        self.__nome = ""
        self.__foto = ""
        self.__bio = ""
        self.__obras = []

        self.set_nome(nome)
        self.set_foto(foto)
        self.set_bio(bio)
        self.set_obras(obras)

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_foto(self, foto):
        self.__foto = foto

    def get_foto(self):
        return "artistas/" + self.__foto

    def set_bio(self, bio):
        self.__bio = bio

    def get_bio(self):
        return self.__bio

    def set_obras(self, obras):
        self.__obras = obras

    def get_obras(self):
        return self.__obras