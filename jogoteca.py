from flask import Flask, render_template, request, redirect
from werkzeug.utils import redirect

from modelos.Jogo import Jogo

jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('Bomba Patch', 'Futebol', 'PS2')
lista_jogos = [jogo1, jogo2]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('lista.html', titulo='jogos', jogos=lista_jogos)

@app.route('/novoJogo')
def cadastrar_jogo():
    return render_template('novo.html', titulo='Cadastro de Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista_jogos.append(jogo)
    return redirect('/')


app.run(debug=True)