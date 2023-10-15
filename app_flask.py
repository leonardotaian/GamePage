from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__, template_folder='templates')
app.secret_key = 'tentedescobrir'


usuarios = {'leonardo' : '123',
            'adenilde' : '123',
            'rafael' : '123',
            'elias' : '123',
            'thoday' : '123',
            'cleber' : '123',
            'erik' : '123',
            'bruno' : '123'
            }

@app.route('/')
def inicio():
    return render_template('login.html')

@app.route ('/login.html', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    
    if username in usuarios and usuarios[username] == password:
        session['username'] = username
        return render_template('perfil.html')
    
@app.route('/cadastro.html')
def cadastro():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        usuarios['username'] = 'password'
        
        return render_template('login.html')
        

@app.route('/perfil.html')
def perfil():
    if 'username' in session:
        return f'Olá, {session["username"]}! Bem-vindo ao seu perfil.'
    
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))      

if __name__ == '__main__':
    app.run(debug=True)   