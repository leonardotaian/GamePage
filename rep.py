import sqlite3

def verif(email):
    try:
        conn = sqlite3.connect("user.db")
        cursor = conn.cursor()
        cursor.execute(f'SELECT email FROM usuario WHERE email = "{email}"')
        email_existente = cursor.fetchone()
        conn.close()
        if email_existente is None:
            email_duplo = False
        else:
            email_duplo = True
        return email_duplo
    except:
        msg = ("Erro na conexão do banco")
        return msg
    
def gerar_id():
    try:
        conn = sqlite3.connect("user.db")
        cursor = conn.cursor()
        cursor.execute('SELECT MAX(id) FROM usuario')
        ultimo_id = cursor.fetchone()[0]
        conn.close()
        if ultimo_id is None:
            novo_id = 1
        else:
            novo_id = ultimo_id + 1
        return novo_id
    except Exception as e:
        print(f"Erro ao gerar ID: {e}")
        return False
    
def login(email,senha):
    try:
        conn = sqlite3.connect("user.db")
        cursor = conn.cursor()
        select = f'SELECT * FROM usuario WHERE email = "{email}" and senha = "{senha}"'
        cursor.execute(select)
        usuario = cursor.fetchall()
        conn.close()
        return usuario
    except:
        False

def cadastro(nome, email, senha):
    try:
        id = gerar_id()
        conn = sqlite3.connect("user.db")
        cursor = conn.cursor()
        select = f'INSERT INTO usuario (id, nome, email, senha) VALUES ({id}, "{nome}", "{email}", "{senha}")'
        cursor.execute(select)
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        print(f"Erro ao cadastrar usuário: {e}")
        return False