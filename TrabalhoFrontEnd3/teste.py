from lista import lista
from get_objs_list import get_autor_obj_list, get_obra_obj_list, get_categoria_obj_list, get_comentario_obj_list, get_exibicao_obj_list

listinha = get_exibicao_obj_list(lista)

contador = 1

while contador < len(listinha):
    print(listinha[contador].get_nome())
    contador += 1