from flask import Flask, render_template
from conferencia import Conferencia,pick_conferencia
from palestrante import Palestrante
from artigo import Artigo
import json

with open("conferencias.json") as f:
    dados_carregados = json.load(f)

tech_xperience = pick_conferencia(dados_carregados, "TechXperience", "john", "jaron", "cathy")
ai_frontiers_summit = pick_conferencia(dados_carregados, "AIFrontiersSummit", "andrew", "fei_fei", "demis")
cyber_next = pick_conferencia(dados_carregados, "CyberNext", "bruce", "mikko", "theresa")


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', tech_xperience = tech_xperience, ai_frontiers_summit = ai_frontiers_summit, cyber_next = cyber_next)

@app.route('/conferencia/<int:id>')
def conferencia(id):
    if id == 1:
        conferencia = tech_xperience
    else:
        if id == 2:
            conferencia = ai_frontiers_summit
        else:
            if id == 3:
                conferencia = cyber_next
            else:
                return "conferencia inexistente"
    return render_template('conferencia.html', conferencia = conferencia, id = id)

@app.route('/artigo/<int:id>')
def artigo(id):
    if id == 1:
        artigo = tech_xperience.get_artigo()
    else:
        if id == 2:
            artigo = ai_frontiers_summit.get_artigo()
        else:
            if id == 3:
                artigo = cyber_next.get_artigo()
            else:
                return "artigo inexistente"
    return render_template('artigo.html', artigo = artigo, id = id)