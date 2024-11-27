from autor import Autor
from obra import Obra
from categoria import Categoria
from comentario import Comentario
from exibicao import Exibicao

def get_autor_obj_list(lista):
    autores = []
    autores.append(None)
    lista_atores = lista["autores"]

    lenght = len(lista_atores)
    contador = 1
    while contador <= lenght:
        autores.append( Autor(
                                lista_atores[contador]["nome"],
                                lista_atores[contador]["foto"],
                                lista_atores[contador]["biografia"],
                                lista_atores[contador]["obras"]
                                )
        )
        contador += 1

    return autores

def get_obra_obj_list(lista):
    obras= []
    obras.append(None)
    lista_obras = lista["obras"]

    lenght = len(lista_obras)
    contador = 1
    while contador <= lenght:
        obras.append( Obra(
                            lista_obras[contador]["nome"],
                            lista_obras[contador]["img"],
                            lista_obras[contador]["descricao"],
                            lista_obras[contador]["categoria"],
                            lista_obras[contador]["autor"],
                            lista_obras[contador]["data_texto"],
                            lista_obras[contador]["leilao"],
                            lista_obras[contador]["exibicao"],
                            lista_obras[contador]["comentarios"]
                            )
        )
        contador += 1

    return obras

def get_categoria_obj_list(lista):
    categorias = []
    categorias.append(None)
    lista_categorias = lista["categorias"]

    lenght = len(lista_categorias)
    contador = 1
    while contador <= lenght:
        categorias.append( Categoria(
                                        contador,
                                        lista_categorias[contador]
                                        )
                                    
        )
        contador += 1

    return categorias

def get_comentario_obj_list(lista):
    comentarios = []
    comentarios.append(None)
    lista_comentarios = lista["comentarios"]

    lenght = len(lista_comentarios)
    contador = 1
    while contador <= lenght:
        comentarios.append( Comentario(
                                        lista_comentarios[contador]["usuario"],
                                        lista_comentarios[contador]["data"],
                                        lista_comentarios[contador]["mensagem"],
                                        lista_comentarios[contador]["lance"],
                                        lista_comentarios[contador]["lance_valor"]
                                        )
                                    
        )
        contador += 1

    return comentarios

def get_exibicao_obj_list(lista):
    exibicoes = []
    exibicoes.append(None)
    lista_exibicoes = lista["exibicoes"]

    lenght = len(lista_exibicoes)
    contador = 1
    while contador <= lenght:
        exibicoes.append( Exibicao(
                                        lista_exibicoes[contador]["nome"],
                                        lista_exibicoes[contador]["local"],
                                        lista_exibicoes[contador]["data"],
                                        lista_exibicoes[contador]["curador"],
                                        lista_exibicoes[contador]["obras"],
                                        )
                                    
        )
        contador += 1

    return exibicoes