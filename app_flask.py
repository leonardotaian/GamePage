from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)



@app.route('/')
def login():
    if request.method == 'POST':
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        nome = request.form['nome']
        senha = request.form['senha']
        print(nome)
        print(senha)
        select = 'SELECT email, senha FROM usuarios WHERE email = "'+nome+'" and senha = "'+senha+'"'
        cursor.execute(select)
        result = cursor.fetchall
        if len(result) == 0:
            print("Credenciais inválidas")
        else:
            user = 'SELECT * FROM usuarios WHERE nome = "'+nome+'"'
            cursor.execute(user)
            user = cursor.fetchall()
            print(user)
            return render_template('perfil.html')
    return render_template('login.html')


app.run(debug=True)
