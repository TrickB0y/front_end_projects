from flask import Flask, render_template
from lanche import Lanche,pick_lanche
import json

with open("lanches.json", "r") as f:
    dados_carregados = json.load(f)

pao_de_queijo = pick_lanche(dados_carregados, "pao_de_queijo")
joelho = pick_lanche(dados_carregados, "joelho")
pastel = pick_lanche(dados_carregados, "pastel")
coxinha = pick_lanche(dados_carregados, "coxinha")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detalhes/<int:id>')
def details(id):
    if id == 1:
        lanche = pao_de_queijo
    else:
        if id == 2:
            lanche = joelho
        else:
            if id == 3:
                lanche = pastel
            else:
                if id == 4:
                    lanche = coxinha
                else:
                    return "lanche inexistente"
    return render_template('detalhes.html', lanche = lanche )