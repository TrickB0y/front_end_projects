import json

dados = {
    "pao_de_queijo": {
        "nome": "Pão de queijo",
        "descricao": "Nosso autêntico pão de queijo é feito com ingredientes selecionados, garantindo uma crocância por fora e uma maciez irresistível por dentro. Feito com o melhor queijo Minas, ele é perfeito para acompanhar o seu café da manhã ou lanche da tarde. Cada mordida traz o sabor inconfundível do Brasil, com aquele toque caseiro que lembra os momentos especiais em família. Experimente e sinta o conforto e a tradição em cada pedaço!",
        "preco": 2.0,
        "nome_foto": "pao-de-queijo.jpeg"
    },
    "joelho": {
        "nome": "Joelho",
        "descricao": "Nosso joelho de presunto e queijo é o salgado perfeito para qualquer hora do dia. Feito com uma massa macia e levemente dourada, ele é recheado generosamente com presunto suculento e queijo derretido, proporcionando uma combinação deliciosa a cada mordida. Este clássico salgado, também conhecido como \"italianinho\" em algumas regiões, é assado na perfeição para garantir um equilíbrio ideal entre sabor e textura. Ideal para um lanche rápido ou acompanhado de um café fresquinho, o joelho é um favorito que nunca sai de moda.",
        "preco": 7.0,
        "nome_foto": "joelho.jpg"
    },
    "pastel": {
        "nome": "Pastel",
        "descricao": "Nosso pastel crocante é um verdadeiro clássico das feiras e lanchonetes brasileiras. Preparado com uma massa fina e dourada, ele é frito na hora para garantir a crocância perfeita. Recheado com opções que vão do tradicional carne moída, queijo, ou frango com catupiry, até os mais criativos, como camarão ou queijo com goiabada, cada pastel é uma explosão de sabor. Perfeito para matar a fome a qualquer hora do dia, acompanhado de um suco gelado ou aquele refrigerante, nosso pastel é irresistível do primeiro ao último pedaço.",
        "preco": 5.5,
        "nome_foto": "pastel.jpeg"
    },
    "coxinha": {
        "nome": "Coxinha",
        "descricao": "Nossa coxinha tradicional é o salgado perfeito para os amantes de um bom lanche brasileiro. Feita com uma massa leve e saborosa, é recheada com frango desfiado temperado na medida certa e um toque de requeijão cremoso, criando um equilíbrio delicioso entre sabor e textura. Frita até ficar dourada e crocante por fora, cada coxinha é uma verdadeira tentação, com um interior suculento que derrete na boca. Seja como um lanche rápido, ou para compartilhar em momentos especiais, a coxinha é sempre uma escolha que agrada a todos.",
        "preco": 6.0,
        "nome_foto": "coxinha.jpeg"
    }
}

# Salvando em arquivo JSON
with open("lanches.json", "w") as f:
    json.dump(dados, f, indent= 4)

with open("lanches.json", "r") as f:
    dados_carregados = json.load(f)

print(dados_carregados["pao_de_queijo"]["nome"])