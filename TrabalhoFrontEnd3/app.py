from flask import Flask, render_template
from lista import lista
from get_objs_list import get_obra_obj_list, get_categoria_obj_list, get_autor_obj_list, get_comentario_obj_list, get_exibicao_obj_list

categorias = get_categoria_obj_list(lista)
autores = get_autor_obj_list(lista)
obras = get_obra_obj_list(lista)
comentarios = get_comentario_obj_list(lista)
exibicoes = get_exibicao_obj_list(lista)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", obras = obras, categorias = categorias, autores = autores)

@app.route('/obra/<int:id>')
def obra(id):
    return render_template("obra.html", id = id, obras = obras, autores = autores, categorias = categorias, comentarios = comentarios)

@app.route('/artista/<int:id>')
def artista(id):
    return render_template("artista.html", id = id, autores = autores, obras = obras, categorias = categorias)

@app.route('/exibicoes')
def exibicoes_home():
    return render_template("exibicoes.html", exibicoes = exibicoes)

@app.route('/detalhes-exibicao/<int:id>')
def detalhes_exibicao(id):
    return render_template("detalhes-exibicao.html", id = id , exibicoes = exibicoes, obras = obras)

@app.route('/leiloes')
def leiloes():
    return render_template("leiloes.html", obras = obras, categorias = categorias, autores = autores)

@app.route('/comentario/<int:id>')
def comentario(id):
    return render_template("comentario.html", id = id, comentarios = comentarios)