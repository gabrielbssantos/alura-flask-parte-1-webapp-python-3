from flask import Flask, render_template

app = Flask(__name__)

class Jogo:
    def __init__(self, nome, categoria, console) -> None:
        self.nome = nome
        self.categoria = categoria
        self.console = console

@app.route('/inicio')
def ola():
    jogo_1 = Jogo('Super mario', 'Ação', 'SNES')
    jogo_2 = Jogo('Pokemon', 'RPG', 'GBA')
    jogo_3 = Jogo('Mortal Kombat', 'Luta', 'SNES')

    lista_jogos = [jogo_1, jogo_2, jogo_3]
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)

app.run()