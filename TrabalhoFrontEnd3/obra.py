class Obra:
    def __init__(
            self,
            nome = "",
            img = "",
            desc = "",
            categoria = 0,
            autor = 0,
            data = "",
            leilao = False,
            exibicao = False,
            comentarios = []
        ):

        self.__nome = ""
        self.__img = ""
        self.__desc = ""
        self.__categoria = 0
        self.__autor = 0
        self.__data = ""
        self.__leilao = False
        self.__exibicao = False
        self.__comentarios = []

        self.set_nome(nome)
        self.set_img(img)
        self.set_desc(desc)
        self.set_categoria(categoria)
        self.set_autor(autor)
        self.set_data(data)
        self.set_leilao(leilao)
        self.set_exibicao(exibicao)
        self.set_comentarios(comentarios)
        

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_img(self, img):
        self.__img = img

    def get_img(self):
        return "obras/" + self.__img
    
    def set_desc(self, desc):
        self.__desc = desc

    def get_desc(self):
        return self.__desc

    def set_categoria(self, categoria):
        self.__categoria = categoria

    def get_categoria(self):
        return self.__categoria

    def set_autor(self, autor):
        self.__autor = autor

    def get_autor(self):
        return self.__autor

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_leilao(self, leilao):
        self.__leilao = leilao

    def get_leilao(self):
        return self.__leilao

    def set_exibicao(self, exibicao):
        self.__exibicao = exibicao

    def get_exibicao(self):
        return self.__exibicao
    
    def set_comentarios(self, comentarios):
        self.__comentarios = comentarios

    def get_comentarios(self):
        return self.__comentarios