from palestrante import pick_palestrante
from artigo import pick_artigo

class Conferencia:
    def __init__(
            self,
            nome = "",
            desc = "",
            tema = "",
            local = "",
            data_texto = "",
            regras = "",
            premio = "",
            organizador = "",
            palestrantes = [],
            artigo = None
            ):
        
        self.__nome = ""
        self.__desc = ""
        self.__tema = ""
        self.__local = ""
        self.__data_texto = ""
        self.__regras = ""
        self.__premio = ""
        self.__organizador = ""
        self.__palestrantes = []
        self.__artigo = None

        self.set_nome(nome)
        self.set_desc(desc)
        self.set_tema(tema)
        self.set_local(local)
        self.set_data_texto(data_texto)
        self.set_regras(regras)
        self.set_premio(premio)
        self.set_organizador(organizador)
        self.set_palestrantes(palestrantes)
        self.set_artigo(artigo)

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome
    
    def set_desc(self, desc):
        self.__desc = desc

    def get_desc(self):
        return self.__desc
    
    def set_tema(self, tema):
        self.__tema = tema

    def get_tema(self):
        return self.__tema
    
    def set_local(self, local):
        self.__local = local

    def get_local(self):
        return self.__local
    
    def set_data_texto(self, data_texto):
        self.__data_texto = data_texto

    def get_data_texto(self):
        return self.__data_texto
    
    def set_regras(self, regras):
        self.__regras = regras

    def get_regras(self):
        return self.__regras
    
    def set_premio(self, premio):
        self.__premio = premio

    def get_premio(self):
        return self.__premio
    
    def set_organizador(self, organizador):
        self.__organizador = organizador

    def get_organizador(self):
        return self.__organizador
    
    def set_palestrantes(self, palestrantes):
        self.__palestrantes = palestrantes

    def get_palestrantes(self):
        return self.__palestrantes
    
    def set_artigo(self, artigo):
        self.__artigo = artigo

    def get_artigo(self):
        return self.__artigo
    
def pick_conferencia(dicionario, nome_conferencia, palestrante_1, palestrante_2, palestrante_3):

    palestrantes = [ 
        pick_palestrante(dicionario, nome_conferencia, palestrante_1),
        pick_palestrante(dicionario, nome_conferencia, palestrante_2),
        pick_palestrante(dicionario, nome_conferencia, palestrante_3)
        ]
    
    artigo = pick_artigo(dicionario, nome_conferencia)

    return Conferencia(dicionario["conferencias"][nome_conferencia]["nome"],
                    dicionario["conferencias"][nome_conferencia]["desc"],
                    dicionario["conferencias"][nome_conferencia]["tema"],
                    dicionario["conferencias"][nome_conferencia]["local"],
                    dicionario["conferencias"][nome_conferencia]["data_texto"],
                    dicionario["conferencias"][nome_conferencia]["regras"],
                    dicionario["conferencias"][nome_conferencia]["premio"],
                    dicionario["conferencias"][nome_conferencia]["organizador"],
                    palestrantes,
                    artigo
                )