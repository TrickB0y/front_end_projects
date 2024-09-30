class Palestrante:
    def __init__(
            self,
            nome_desc = "",
            desc = "",
            nome_foto = ""
            ):
        
        self.__nome_desc = ""
        self.__desc = ""
        self.__nome_foto = ""

        self.set_nome_desc(nome_desc)
        self.set_desc(desc)
        self.set_nome_foto(nome_foto)

    def set_nome_desc(self, nome_desc):
        self.__nome_desc = nome_desc
    
    def get_nome_desc(self):
        return self.__nome_desc
    
    def set_desc(self, desc):
        self.__desc = desc
    
    def get_desc(self):
        return self.__desc
    
    def set_nome_foto(self, nome_foto):
        self.__nome_foto = nome_foto
    
    def get_nome_foto(self):
        return self.__nome_foto
    
def pick_palestrante(dicionario, nome_conferencia, nome_palestrante):
    return Palestrante(dicionario["conferencias"][nome_conferencia]["palestrantes"][nome_palestrante]["nome_desc"],
                    dicionario["conferencias"][nome_conferencia]["palestrantes"][nome_palestrante]["desc"],
                    dicionario["conferencias"][nome_conferencia]["palestrantes"][nome_palestrante]["nome_foto"]
                )