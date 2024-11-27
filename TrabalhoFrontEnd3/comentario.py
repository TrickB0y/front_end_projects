class Comentario:
    def __init__(
            self,
            usuario = "",
            data = "",
            mensagem = "",
            lance = False,
            valor_lance = 0.0
        ):
        
        self.__usuario = ""
        self.__data = ""
        self.__mensagem = ""
        self.__lance = False
        self.__valor_lance = 0.0

        self.set_usuario(usuario)
        self.set_data(data)
        self.set_mensagem(mensagem)
        self.set_lance(lance)
        self.set_valor_lance(valor_lance)

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def get_usuario(self):
        return self.__usuario
    
    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data
    
    def set_mensagem(self, mensagem):
        self.__mensagem = mensagem

    def get_mensagem(self):
        return self.__mensagem
    
    def set_lance(self, lance):
        self.__lance = lance

    def get_lance(self):
        return self.__lance
    
    def set_valor_lance(self, valor_lance):
        self.__valor_lance = valor_lance

    def get_valor_lance(self):
        return self.__valor_lance
    
    