from flask import Flask, render_template
from flask_login import login_manager
from flask_sqlalchemy import SQLALchemy




db = SQLALchemy()

app = Flask(__name__)

@app.route("/")
def cs():
    return "Eae men kk!"

@app.route("/personagem/<int:personagem_id>")
def mostra_personagem(personagem_id):
    return render_template('personagem.html', **personagens[personagem_id])

app.run(debug=True)