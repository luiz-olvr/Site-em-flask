from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    titulo = "Gestão de usuarios"
    usuarios = [
        {"nome": "joao", "membro_ativo": True},
        {"nome": "Luiz", "membro_ativo": True},
        {"nome": "Maria", "membro_ativo": False},
    ]
    return render_template('index.html', titulo = titulo, usuarios = usuarios)

@app.route('/sobre')
def pagina_sobre():
    return "Sobre"


if __name__ == '__main__':
    app.run(debug=True)