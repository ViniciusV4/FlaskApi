from flask import Flask, render_template, request, redirect, session, flash, url_for

from modelos.Jogo import Jogo
from modelos.Usuario import Usuario

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('Bomba Patch', 'Futebol', 'PS2')
lista_jogos = [jogo1, jogo2]

usuario1 = Usuario("Marcos", "MarquinDelas", "alohomora")
usuario2 = Usuario("Thomas", "ToninDele", "bruno")
usuario3 = Usuario("Kae", "KaeDela", "uhum")

usuarios = {
    usuario1.nickname : usuario1,
    usuario2.nickname : usuario2,
    usuario3.nickname : usuario3
}

app = Flask(__name__)
app.secret_key = 'eoMarcos'

@app.route('/')
def index():
    return render_template('lista.html', titulo='jogos', jogos=lista_jogos)

@app.route('/novo_jogo')
def cadastrar_jogo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('cadastrar_jogo')))
    return render_template('novo.html', titulo='Cadastro de Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista_jogos.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' Usuário logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)

    else:
        flash(' Usuário não logado')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout realizado com sucesso!')
    return redirect(url_for('index'))


app.run(debug=True)