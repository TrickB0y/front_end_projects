class Exibicao:
    def __init__(
            self,
            nome = "",
            local = "",
            data = "",
            curador = "",
            obras = []
        ):

        self.__nome = ""
        self.__local = ""
        self.__data = ""
        self.__curador = ""
        self.__obras = []

        self.set_nome(nome)
        self.set_local(local)
        self.set_data(data)
        self.set_curador(curador)
        self.set_obras(obras)

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome
    
    def set_local(self, local):
        self.__local = local

    def get_local(self):
        return self.__local
    
    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data
    
    def set_curador(self, curador):
        self.__curador = curador

    def get_curador(self):
        return self.__curador
    
    def set_obras(self, obras):
        self.__obras = obras

    def get_obras(self):
        return self.__obras
    