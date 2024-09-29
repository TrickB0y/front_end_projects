import json
from flask import url_for

class Lanche:
    def __init__(self, nome = "", preco = 0.0, descricao = "", foto_nome = ""):
        self.nome = ""
        self.preco = 0.0
        self.descricao = ""
        self.foto_nome = ""

        self.set_nome(nome)
        self.set_preco(preco)
        self.set_descricao(descricao)
        self.set_foto_nome(foto_nome)

    def set_nome(self, nome):
        self.nome = nome

    def set_preco(self, preco):
        self.preco = preco

    def set_descricao(self, descricao):
        self.descricao = descricao

    def set_foto_nome(self, foto_nome):
        self.foto_nome = foto_nome

    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco

    def get_descricao(self):
        return self.descricao
    
    def get_foto_nome(self):
        return self.foto_nome
    
    def foto_lanche(self):
        return url_for( 'static' , filename='imgs/' + self.get_foto_nome())
    
def pick_lanche(dicionario, nome_lanche):
    return Lanche(dicionario[nome_lanche]["nome"],
                    dicionario[nome_lanche]["preco"],
                    dicionario[nome_lanche]["descricao"],
                    dicionario[nome_lanche]["nome_foto"]
                )