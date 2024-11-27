class Categoria:
    def __init__(
            self,
            id = 0,
            nome = ""
        ):
        
        self.__id = 0
        self.__nome = ""

        self.set_id(id)
        self.set_nome(nome)

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome