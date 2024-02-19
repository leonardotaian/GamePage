import sqlite3

def gerar_id():
    try:
        conn = sqlite3.connect("user.db")
        cursor = conn.cursor()
        select = f'SELECT seq FROM sql_sequence WHERE name = "user"'
        cursor.execute(select)
        ultimo_id = cursor.fetchall()
        conn.close()
        novo_id = ultimo_id + 1
        return novo_id
    except:
        False


def login(email,senha):
    try:
        conn = sqlite3.connect("user.db")
        cursor = conn.cursor()
        select = f'SELECT * FROM user WHERE email = "{email}" and senha = "{senha}"'
        cursor.execute(select)
        usuario = cursor.fetchall()
        conn.close()
        return usuario
    except:
        False

def cadastro(nome,email,senha):
    try:
        id = gerar_id()
        conn = sqlite3.connect("user.db")
        cursor = conn.cursor()
        select = f'INSERT INTO user (id,nome,email,senha) VALUES ({id},"{nome}","{email}","{senha}")'
        cursor.execute(select)
        conn.commit()
        conn.close()
        msg = "Dados Gravados com sucesso"
        return msg
    except:
        False
