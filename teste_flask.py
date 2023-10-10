from flask import Flask, render_template

personagens = {
    1:{
        "nome": "SAS",
        "altura": 1.78,
        "origem": "Escócia",
        "imagem": "https://www.sitecs.net/images/players/sas_a.jpg"
    },
    2: {
        "nome": "GSG9",
        "altura": 1.76,
        "origem": "Alemanha",
        "imagem": "https://www.sitecs.net/images/players/gsg9_a.jpg"
    },
    3: {
        "nome": "GIGN",
        "altura": 1.82,
        "origem": "França",
        "imagem": "https://www.sitecs.net/images/players/gign_a.jpg"
    },
    4: {
        "nome": "Terror",
        "altura": 1.90,
        "origem": "Egito",
        "imagem": "https://www.sitecs.net/images/players/terror_a.jpg"
    },
    5: {
        "nome": "Arab",
        "altura": 1.92,
        "origem": "Palestina",
        "imagem": "https://www.sitecs.net/images/players/arab_a.jpg"   
    },
    6: {
        "nome": "Guerrila",
        "altura": 1.76,
        "origem": "Cuba",
        "imagem": "https://www.sitecs.net/images/players/gor_a.jpg"   
    },
    7: {
        "nome": "Artic",
        "altura": 1.86,
        "origem": "Rússia",
        "imagem": "https://www.sitecs.net/images/players/arctic_a.jpg"   
    },
    8: {
        "nome": "Seal Team Six",
        "altura": 1.82,
        "origem": "EUA",
        "imagem": "https://www.sitecs.net/images/players/urban_a.jpg"   
    },
    9: {
        "nome": "VIP",
        "altura": 1.68,
        "origem": "Inglaterra",
        "imagem": "https://www.sitecs.net/images/players/vip_a.jpg"   
    },
    10: {
        "nome": "Hostage",
        "altura": 1.82,
        "origem": "Desconhecido",
        "imagem": "https://www.sitecs.net/images/players/hostage1_a.jpg"   
    }
}


app = Flask(__name__)

@app.route("/")
def cs():
    return personagens[1]["nome"]

@app.route("/personagem/<int:personagem_id>")
def mostra_personagem(personagem_id):
    return render_template('personagem.html', **personagens[personagem_id])

app.run(debug=True)