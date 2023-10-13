from flask import Flask, render_template

personagens = {
    1:{
        "nome": "SAS",
        "origem": "Escócia",
        "imagem": "https://www.sitecs.net/images/players/sas_a.jpg"
    },
    2: {
        "nome": "GSG9",
        "origem": "Alemanha",
        "imagem": "https://www.sitecs.net/images/players/gsg9_a.jpg"
    },
    3: {
        "nome": "GIGN",
        "origem": "França",
        "imagem": "https://www.sitecs.net/images/players/gign_a.jpg"
    },
    4: {
        "nome": "Terror",
        "origem": "Egito",
        "imagem": "https://www.sitecs.net/images/players/terror_a.jpg"
    },
    5: {
        "nome": "Arab",
        "origem": "Palestina",
        "imagem": "https://www.sitecs.net/images/players/arab_a.jpg"   
    },
    6: {
        "nome": "Guerrila",
        "origem": "Cuba",
        "imagem": "https://www.sitecs.net/images/players/gor_a.jpg"   
    },
    7: {
        "nome": "Artic",
        "origem": "Rússia",
        "imagem": "https://www.sitecs.net/images/players/arctic_a.jpg"   
    },
    8: {
        "nome": "Seal Team Six",
        "origem": "EUA",
        "imagem": "https://www.sitecs.net/images/players/urban_a.jpg"   
    },
    9: {
        "nome": "VIP",
        "origem": "Inglaterra",
        "imagem": "https://www.sitecs.net/images/players/vip_a.jpg"   
    },
    10: {
        "nome": "Hostage",
        "origem": "Desconhecido",
        "imagem": "https://www.sitecs.net/images/players/hostage1_a.jpg"   
    }
}

usuarios = {
    'nome' : 'leonardo', 'senha' : '1234', 'email' : 'leonardotaianav@outlook.com' 
}


app = Flask(__name__)

@app.route("/")
def cs():
    return personagens[1]["nome"]

@app.route("/personagem/<int:personagem_id>")
def mostra_personagem(personagem_id):
    return render_template('personagem.html', **personagens[personagem_id])

app.run(debug=True)