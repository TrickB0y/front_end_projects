class Artigo:
    def __init__(
            self,
            nome = "",
            autor = "",
            foto = "",
            resumo = "",
            intro = "",
            metodologia = "",
            resultados = "",
            conclusao = ""
            ):
        
        self.__nome = ""
        self.__autor = ""
        self.__foto = ""
        self.__resumo = "",
        self.__intro = "",
        self.__metodologia = "",
        self.__resultados = "",
        self.__conclusao = ""

        self.set_nome(nome)
        self.set_autor(autor)
        self.set_foto(foto)
        self.set_resumo(resumo)
        self.set_intro(intro)
        self.set_metodologia(metodologia)
        self.set_resultados(resultados)
        self.set_conclusao(conclusao)

    def set_nome(self, nome):
        self.__nome = nome
    
    def get_nome(self):
        return self.__nome
    
    def set_autor(self, autor):
        self.__autor = autor
    
    def get_autor(self):
        return self.__autor
    
    def set_foto(self, foto):
        self.__foto = foto
    
    def get_foto(self):
        return self.__foto
    
    def set_resumo(self, resumo):
        self.__resumo = resumo
    
    def get_resumo(self):
        return self.__resumo
    
    def set_intro(self, intro):
        self.__intro = intro
    
    def get_intro(self):
        return self.__intro
    
    def set_metodologia(self, metodologia):
        self.__metodologia = metodologia
    
    def get_metodologia(self):
        return self.__metodologia
    
    def set_resultados(self, resultados):
        self.__resultados = resultados
    
    def get_resultados(self):
        return self.__resultados
    
    def set_conclusao(self, conclusao):
        self.__conclusao = conclusao
    
    def get_conclusao(self):
        return self.__conclusao
    


    
def pick_artigo(dicionario, nome_conferencia):
    return Artigo(dicionario["conferencias"][nome_conferencia]["artigo"]["nome"],
                    dicionario["conferencias"][nome_conferencia]["artigo"]["autor"],
                    dicionario["conferencias"][nome_conferencia]["artigo"]["foto"],
                    dicionario["conferencias"][nome_conferencia]["artigo"]["resumo"],
                    dicionario["conferencias"][nome_conferencia]["artigo"]["intro"],
                    dicionario["conferencias"][nome_conferencia]["artigo"]["metodologia"],
                    dicionario["conferencias"][nome_conferencia]["artigo"]["resultados"],
                    dicionario["conferencias"][nome_conferencia]["artigo"]["conclusao"]
                )