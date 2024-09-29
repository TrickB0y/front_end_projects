from lanche import pick_lanche, Lanche
import json
with open("lanches.json", "r") as f:
    dados_carregados = json.load(f)

pao_de_queijo = pick_lanche(dados_carregados, "pao_de_queijo")

print(pao_de_queijo.get_nome())