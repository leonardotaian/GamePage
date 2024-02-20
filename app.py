from flask import Flask, render_template, request, redirect, url_for, session
from flask_login import login_user, logout_user, current_user
import sqlite3
import rep

app = Flask(__name__, static_folder='static')



@app.route('/')
def home():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        usuario = rep.login(email,senha)
        if len(usuario) != 0:
            id = usuario[0][0]
            nome = usuario[0][1]
            email = usuario[0][2]
            senha = usuario[0][3]
            #user_dados = User(id, nome, email, senha)
            #login_user(user_dados)
            return render_template("perfil.html")
        else:
            return render_template("login.html")
    return render_template("login.html")

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == "POST":
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        email_duplo = rep.verif(email=email)
        if not email_duplo:
            cadastro_result = rep.cadastro(nome=nome, email=email, senha=senha)
            if cadastro_result:
                return render_template('perfil.html', usuario=nome)
            else:
                return "Erro ao cadastrar usuário"
    
    return render_template('cadastro.html')
    

app.run(debug=True)
